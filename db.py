"""SQLite connection for the notes app."""

import sqlite3

DATABASE = "notes.db"


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE)
    conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT NOT NULL)")
    return conn
