import sqlite3

VALGEIR = "Valgeir_Palsson.db"

def get_connection(): # Connect/create DB
    conn = sqlite3.connect(VALGEIR)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    return conn, cursor

def setup_tables(cursor, conn): # Create 2 tables (users(ID,name,age))(tasks(ID,title))
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL)
    """)

    cursor.execute("""
   CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        done INTEGER NOT NULL DEFAULT 0,  
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)
    """)

print("Database and tables created!")