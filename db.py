# db.py
import sqlite3

def get_conn():
    return sqlite3.connect("data.db")

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            body TEXT
        )
    """)
    conn.commit()
    conn.close()
