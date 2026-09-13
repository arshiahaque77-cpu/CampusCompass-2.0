"""
Initializes the CampusCompass database.

Run this file once to create the database and all required tables.
"""

import sqlite3


def create_database():
    """ Create the CampusCompass database and required tables. """

    connection = sqlite3.connect("campuscompass.db")
    cursor = connection.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    """)

    # Tasks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    due_date TEXT,
    status TEXT NOT NULL DEFAULT 'Pending',

    FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # Attendance table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        subject_name TEXT NOT NULL,
        classes_attended INTEGER DEFAULT 0,
        total_classes INTEGER DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # Timetable table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS timetable (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        subject_name TEXT NOT NULL,
        day TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        repeat TEXT NOT NULL DEFAULT 'Weekly',


        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)



    # Add repeat column to existing timetable table
    try:
        cursor.execute("""
        ALTER TABLE timetable
        ADD COLUMN repeat TEXT NOT NULL DEFAULT 'Weekly'
        """)
    except sqlite3.OperationalError:
        pass

 
    # Save all changes to the database
    connection.commit()

    # Close the database connection
    connection.close()

    print("Databse and tables created successfully!")


if __name__ == "__main__":
    create_database()
