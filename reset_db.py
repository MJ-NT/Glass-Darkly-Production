import sqlite3

# Connect to the database
conn = sqlite3.connect("game.db")
cursor = conn.cursor()

# Drop existing tables if they exist
cursor.executescript("""
DROP TABLE IF EXISTS user_stats;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS challenges;
""")

# Recreate tables
cursor.executescript("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    story_state INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE user_stats (
    user_id INTEGER PRIMARY KEY,
    watchful INTEGER DEFAULT 1,
    shadowy INTEGER DEFAULT 1,
    dangerous INTEGER DEFAULT 1,
    persuasive INTEGER DEFAULT 1,
    apprehensions INTEGER DEFAULT 0,
    menace INTEGER DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    story_state INTEGER,
    text TEXT,
    option_number INTEGER,
    option_text TEXT,
    stat TEXT,
    difficulty INTEGER,
    success_text TEXT,
    failure_text TEXT,
    next_state_success INTEGER,
    next_state_failure INTEGER,
    apprehension_change_success INTEGER DEFAULT 0,
    apprehension_change_failure INTEGER DEFAULT 0,
    menace_change_success INTEGER DEFAULT 0,
    menace_change_failure INTEGER DEFAULT 0
);
""")

# Commit and close connection
conn.commit()
conn.close()
print("Database reset complete and schema rebuilt.")
