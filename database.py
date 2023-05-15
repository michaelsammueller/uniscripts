import sqlite3
import hashlib

# Connect to SQL database or create database if it doesn't exist
connect = sqlite3.connect('data/astrounauts.db')
cursor = connect.cursor()

# Creation of the 'astronaut' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS astronauts (
        astronaut_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        date_of_birth TEXT,
        role TEXT,
        height REAL,
        nationality TEXT,
        username TEXT,
        password_hash TEXT,
    )
''')

# Creation of the health records table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS health_records (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        astronaut_id INTEGER,
        weight REAL,
        temperature REAL,
        symptoms TEXT,
        radiation_levels REAL,
        blood_pressure TEXT,
        record_date TEXT,
        FOREIGN KEY (astronaut_id) REFERENCES astronauts (astronaut_id),
    )
''')

# Commit changes and close the connection
connect.commit()
connect.close()

print("Database initialised.")