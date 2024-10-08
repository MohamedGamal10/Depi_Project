import sqlite3

def connect_db():
    conn = sqlite3.connect('medical_erp.db')
    return conn

# Connect to SQLite database
conn = sqlite3.connect('medical_erp.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        diagnosis TEXT,
        ssn TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor TEXT,
        appointment_date TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients(id)
    )
''')

conn.commit()
conn.close()
