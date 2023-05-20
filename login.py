import sqlite3
import bcrypt
import getpass

connect = sqlite3.connect('data/securespace.db')
cursor = connect.cursor()

# Collect user input
def collect_user_input():
    username = input("Username: ")
    password = getpass.getpass("Password: ", stream=None)
    return username, password

def register(username, password):
    # Check if user already exists
    cursor.execute('SELECT * FROM user_records WHERE username = ?', (username,))
    if cursor.fetchone():
        print("This user already exists\n")
        return
    
    # Encrypt user password for storage
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert new user record into database
    cursor.execute('INSERT INTO user_records (username, encrypted_password) VALUES (?, ?)', (username, password_hash))
    connect.commit()
    print("User registered successfully!\n")

def login(username, password):
    # Retrieve password for username
    cursor.execute('SELECT encrypted_password FROM user_records WHERE username = ?', (username,))
    result = cursor.fetchone()
    if result:
        stored_password = result[0]
        # Matching stored password to entered password
        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            print("Login successful!\n")
            return True
        print("Invalid username or password.\n")




