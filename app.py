import os, random
from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_cors import CORS
from flask_session import Session
from helpers import get_db_connection, login_required
from werkzeug.security import check_password_hash, generate_password_hash

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
debug = os.getenv("DEBUG", "False") == "True"
port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)
CORS(app)  # Allow frontend requests (ChatGPT suggestion)

# Secret key for securely signing the session cookies
# Assign using os library and access secret key from .env file by key (i.e. key-value pair)
app.secret_key = os.environ.get("SECRET_KEY")

# Flask-Session configuration
app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=3)
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_FILE_DIR"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flask_session")
app.config["SESSION_USE_SIGNER"] = True  # Adds HMAC signing to session IDs - prevents tampering
app.config["SESSION_COOKIE_HTTPONLY"] = True  # Makes cookies inaccessible to JavaScript
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"  # Prevents CSRF (Cross-Site Request Forgery) attacks
Session(app)

# Define constant for scaler
SCALER = 0.6

@app.route("/")
@login_required
def index():
    """Render the home page with user data"""

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE user_id = ?", (session["user_id"],))
    user = cursor.fetchone()
    conn.close()

    return render_template("index.html", user=user)


@app.route("/about")
def about():
    # Only ever reached via GET
    return render_template("about.html")


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """Manage user account"""

    # Query database for username and password at the start to factor out repeated queries
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users WHERE user_id = ?", (session["user_id"],))
    user = cursor.fetchone()
    conn.close()

    # Ensure user exists (shouldn't be necessary since login_required wrapper is used)
    if not user:
        flash("User not found", "danger")
        return redirect("/logout")

    # Else if user reached route via POST
    if request.method == "POST":
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        # Ensure fields are not empty
        if not current_password or not new_password or not confirmation:
            flash("All fields are required", "danger")
            return redirect("/account")

        # Ensure new password is different from current (i.e. old) password
        if current_password == new_password:
            flash("New password cannot be the same as the old password", "danger")
            return redirect("/account")

        # Ensure new password matches confirmation
        if new_password != confirmation:
            flash("New password and confirmation do not match", "danger")
            return redirect("/account")

        # Ensure current password is correct
        if not check_password_hash(user["password"], current_password):
            flash("Invalid current password", "danger")
            return redirect("/account")

        # Hash new password and update in database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password = ? WHERE user_id = ?", 
                       (generate_password_hash(new_password), session["user_id"]))
        conn.commit()
        conn.close()

        # Flash 'password changed' message
        flash("Password changed successfully", "success")

        # Redirect to account page
        return redirect("/account")

    # Render template with user data
    else:
        return render_template("account.html", user=user)
    

@app.route("/challenge", methods=["GET", "POST"])
@login_required
def challenge():
    """Handle challenge options and outcomes based on user stats and story state"""
    
    conn = get_db_connection()
    cursor = conn.cursor()
    user_id = session["user_id"]

    # If menace is too high, redirect to 'overcome' page
    cursor.execute("SELECT menace FROM user_stats WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    # Fetch username to pass to template.
    cursor.execute("SELECT username FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    # Handle case where user_id not found (even though login_required should prevent this)
    if result is None or user is None:
        conn.close()
        flash("User not found", "danger")
        return redirect("/login")
    if result["menace"] >= 100:
        conn.close()
        return render_template("overcome.html", user=user)

    # Get user's story state
    cursor.execute("SELECT story_state FROM users WHERE user_id = ?", (user_id,))
    # Fetch the --value-- from the dictionary-like row returned by fetchone(), not just the row
    story_state = cursor.fetchone()["story_state"]

    # Get current challenge options based on story state
    cursor.execute("SELECT * FROM challenges WHERE story_state = ?", (story_state,))
    options = cursor.fetchall()

    # If no options are found, display end message
    if not options:
        conn.close()
        return render_template("challenge.html", challenge=None, story_text="""Thank you for playing Through Glass Darkly.
                               
                               If you enjoyed this game and you haven't yet played the game it is based on, 'A House of Many Doors', then I can't recommend doing so enough!
                               
                               You can find HOMD by following the link in the 'About' page. You can restart this game by clicking the 'Restart Game' button below.""")

    if request.method == "POST":
        selected_option = int(request.form.get("option"))
        # Implement generator expression to find chosen option and handle errors with default value None for next() function
        chosen = next((opt for opt in options if opt["option_number"] == selected_option), None)

        # Ensure chosen option is valid
        if not chosen:
            conn.close()
            flash("Invalid choice", "danger")
            return redirect("/challenge")

        # Get user's stat value
        cursor.execute(f"SELECT {chosen['stat']} FROM user_stats WHERE user_id = ?", (user_id,))
        stat_value = cursor.fetchone()[0]

        # Calculate success chance as a percentage
        difficulty = chosen["difficulty"]
        success_chance = min(100, int((SCALER * stat_value) / difficulty * 100))
        rng = random.randint(1, 100)
        success = rng <= success_chance

        # Update apprehensions and story state based on success
        if success:
            story_text = chosen["success_text"]
            next_state = chosen["next_state_success"]
            apprehension_change = chosen["apprehension_change_success"]
            menace_change = chosen["menace_change_success"]
        else:
            story_text = chosen["failure_text"]
            next_state = chosen["next_state_failure"]
            apprehension_change = chosen["apprehension_change_failure"]
            menace_change = chosen["menace_change_failure"]
        
        # Update user's stats in the database
        cursor.execute("UPDATE user_stats SET apprehensions = apprehensions + ?, menace = menace + ? WHERE user_id = ?",
                       (apprehension_change, menace_change, user_id))
        # Update user's story state
        cursor.execute("UPDATE users SET story_state = ? WHERE user_id = ?", (next_state, user_id))

        conn.commit()
        conn.close()

        return render_template("challenge.html", challenge=None, story_text=story_text)

    # If user reached route via GET, fetch user stats and challenge options
    # Fetch all stats once
    cursor.execute("SELECT watchful, shadowy, dangerous, persuasive FROM user_stats WHERE user_id = ?", (user_id,))
    user_stats = cursor.fetchone()

    # Set up dictionary to pass to template
    challenge_data = {
        "text": options[0]["text"],  # Challenge text shared across all options for this story state
        "options": []
    }

    # Iterate through options (stored in challenges.py, and subsequently game.db) to calculate success chances
    for opt in options:
        stat_name = opt["stat"]
        # Use the stat name to get the corresponding value from user_stats
        stat_value = user_stats[stat_name]
        success_chance = int((SCALER * stat_value) / opt["difficulty"] * 100)
        # Cap success chance at 100%
        success_chance = min(success_chance, 100)

        # Populates challenge_data options list
        challenge_data["options"].append({
            "text": opt["option_text"],
            "number": opt["option_number"],
            "stat": stat_name,
            "chance": success_chance
        })

    conn.close()
    return render_template("challenge.html", challenge=challenge_data, story_text=None)



@app.route("/login", methods=["GET", "POST"])
def login():
    """ Log user in"""

    # Get current flashed messages and store in list
    flashes = session.get("_flashes", [])

    # Clear the session completely
    session.clear()

    # Retrieve only the most recent message
    if flashes:  
        session["_flashes"] = [flashes[-1]]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure fields are not empty
        if not username or not password:
            flash("Username and password are required", "danger")
            return redirect("/")
        
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query database for username
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        # Ensure username exists and password is correct
        if user is None or not check_password_hash(user["password"], password):
            flash("Invalid username or password", "danger")
            return redirect("/")

        # Remember which user has logged in
        session["user_id"] = user["user_id"]

        # Flash 'welcome' message
        flash(f"A welcome return, {username}.", "success")

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
    

@app.route("/myself", methods=["GET", "POST"])
@login_required
def myself():
    """Display user profile, stats, and handle stat improvement"""

    conn = get_db_connection()
    cursor = conn.cursor()

    # Instead of a JOIN, get user_stats directly using user_id (stored in session)
    cursor.execute("SELECT * FROM user_stats WHERE user_id = ?", (session["user_id"],))
    user_stats = cursor.fetchone()

    # Then get username from users table using user_id
    cursor.execute("SELECT username FROM users WHERE user_id = ?", (session["user_id"],))
    user = cursor.fetchone()

    story_text = None

    if request.method == "POST":
        stat = request.form.get("stat")
        amount = request.form.get("amount")

        # Ensure valid integer value passed (should be, since dropdown is used in html)
        try:
            amount = int(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive")
        except (ValueError, TypeError):
            return jsonify({"success": False, "error": "Invalid amount"}), 400

        # Check if the user has enough apprehensions
        if amount > user_stats["apprehensions"]:
            return jsonify({"success": False, "error": "Not enough apprehensions"}), 400
        
        # Guard against SQL injection (so f-string safe to use next)
        if stat not in ["watchful", "shadowy", "dangerous", "persuasive"]:
            return jsonify({"success": False, "error": "Invalid stat"}), 400

        # If user has enough apprehensions, update the stat and subtract the resources
        cursor.execute(f"UPDATE user_stats SET {stat} = {stat} + ? WHERE user_id = ?", (amount, session["user_id"],))
        cursor.execute("UPDATE user_stats SET apprehensions = apprehensions - ? WHERE user_id = ?", (amount, session["user_id"]))
        conn.commit()

        # Re-fetch user stats to reflect changes
        cursor.execute("SELECT * FROM user_stats WHERE user_id = ?", (session["user_id"],))
        new_stats = cursor.fetchone()

        # Create story based on the stat improvement
        if stat == "watchful":
            story_text = "In the quiet moments, you reflect, that in the loud, you might act. You have honed your senses to a fine point."
        elif stat == "shadowy":
            story_text = " Subtlety is a caged science. You have made an art of it. Your footsteps are lighter, your hands more deft."
        elif stat == "dangerous":
            story_text = "What thews you have! How impressively they ripple. You have become leaner, sleeker, more powerful."
        elif stat == "persuasive":
            story_text = "A well-chosen word can stay a blade. What, then, can many do? Yours cut like a whetted knife."

        conn.close()
        
        # Return the updated stats and story text as JSON
        return jsonify({
            "success": True,
            "new_stats": {
                "watchful": new_stats["watchful"],
                "shadowy": new_stats["shadowy"],
                "dangerous": new_stats["dangerous"],
                "persuasive": new_stats["persuasive"],
                "apprehensions": new_stats["apprehensions"]
            },
            "story_text": story_text
        })

    # If user reached route via GET, close connection created before conditional
    conn.close()

    return render_template("myself.html", user=user, user_stats=user_stats, story_text=story_text)


@app.route("/overcome", methods=["GET", "POST"])
@login_required
def overcome():
    """Create 'overcome' page to handle restarting the game"""

    conn = get_db_connection()
    cursor = conn.cursor()

    # Get username
    cursor.execute("SELECT username FROM users WHERE user_id = ?", (session["user_id"],))
    user = cursor.fetchone()
    # Handle case where user_id not found (even though login_required should prevent this)
    if user is None:
        conn.close()
        flash("User not found", "danger")
        return redirect("/login")

    # User reached route via POST
    if request.method == "POST":
        # Reset user's stats and story state
        cursor.execute("UPDATE user_stats SET watchful = 1, shadowy = 1, dangerous = 1, persuasive = 1, apprehensions = 0, menace = 0 WHERE user_id = ?", (session["user_id"],))
        cursor.execute("UPDATE users SET story_state = 0 WHERE user_id = ?", (session["user_id"],))
        conn.commit()
        conn.close()
        # Flash 'game reset' message
        flash("Game reset successfully. You may now start again.", "success")
        # Redirect to home page
        return redirect("/")
    
    # If user reached route via GET, close connection created before conditional
    conn.close()

    return render_template("overcome.html", user=user)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user"""

    # Get current flashed messages and store in list
    flashes = session.get("_flashes", [])

    # Clear the session completely
    session.clear()

    # Retrieve only the most recent message
    if flashes:  
        session["_flashes"] = [flashes[-1]]

    # User reached route via POST
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure fields are not empty
        if not username or not password or not confirmation:
            flash("All fields are required", "danger")
            return redirect("/register")
        
        # Ensure password matches confirmation
        elif password != confirmation:
            flash("Passwords do not match", "danger")
            return redirect("/register")
        
        # Ensure username not same as password
        elif username == password:
            flash("Username and password cannot be the same", "danger")
            return redirect("/register")
        
        # Ensure password is at least 5 characters long
        elif len(password) < 5:
            flash("Password must be at least 5 characters long", "danger")
            return redirect("/register")
        
        # Introduce try and except error handling - Ensure username is not already taken
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            existing_user = cursor.fetchone()
            conn.close()

            if existing_user:
                flash("Username already taken", "danger")
                return redirect("/register")
        except Exception as e:
            flash("An error occurred while checking the username. Please try again.", "danger")
            return redirect("/register")

        # Insert new user into game.db using hashed password
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, story_state) VALUES (?, ?, ?)", 
                           (username, generate_password_hash(password), 0))
            conn.commit()

            # Retrieve newly-inserted user_id
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            new_user = cursor.fetchone()

            # Insert new user into user_stats table with default values
            cursor.execute("INSERT INTO user_stats (user_id, watchful, shadowy, dangerous, persuasive, apprehensions) VALUES (?, ?, ?, ?, ?, ?)",
                           (new_user["user_id"], 1, 1, 1, 1, 0))
            conn.commit()
            conn.close()

            # Store the user_id in session for tracking
            session["user_id"] = new_user["user_id"]

            # Flash 'registered' message
            flash(f"Registered successfully, {username}. Welcome to the House.", "success")

            # Redirect to first challenge (i.e. challenge.html with story state 0)
            return redirect("/challenge")

        except Exception as e:
            flash("An error occurred during registration. Please try again.", "danger")
            return redirect("/register")
    
    # User reached route via GET
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Flash 'logged out' message
    flash("Logged out succesfully!", "success")

    # Redirect user to login form
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=debug)