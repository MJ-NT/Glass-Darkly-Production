from flask import redirect, session
from functools import wraps
import sqlite3

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect("game.db")
    conn.row_factory = sqlite3.Row  # Set to Row to allow dictionary-like row access
    return conn

def login_required(f):
    """Decorate routes to require login."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function