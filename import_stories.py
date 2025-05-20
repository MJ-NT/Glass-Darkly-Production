import sqlite3
from challenges import challenges # Import the challenges from the challenges.py file

# Connect to database
conn = sqlite3.connect("game.db")
cursor = conn.cursor()

# Clear old data
cursor.execute("DELETE FROM challenges")

# Insert each challenge
for story in challenges:
    story_state = story["story_state"]
    text = story["text"]

    for i, option in enumerate(story["options"], start=1):
        cursor.execute("""
            INSERT INTO challenges (
                story_state, text, option_number, option_text, stat,
                difficulty, success_text, failure_text,
                next_state_success, next_state_failure,
                apprehension_change_success, apprehension_change_failure,
                menace_change_success, menace_change_failure
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            story_state,
            text,
            i,
            option["text"],
            option["stat"],
            option["difficulty"],
            option["success_text"],
            option["failure_text"],
            option["next_state_success"],
            option["next_state_failure"],
            option["apprehension_change_success"],
            option["apprehension_change_failure"],
            option["menace_change_success"],
            option["menace_change_failure"],
        ))

conn.commit()
conn.close()
print("Stories imported successfully.")