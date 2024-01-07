import sqlite3

# Database Initialization
def connect():
    return sqlite3.connect("database.db")

def create_table(conn):
    cursor = conn.cursor()
    # Create Tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            quantity INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lend_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            user_id INTEGER,
            return_status BOOLEAN DEFAULT 0,
            FOREIGN KEY (book_id) REFERENCES books (id),
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()