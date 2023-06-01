import sqlite3
from cryptography.fernet import Fernet

# Imports from other files
from validation import are_you_sure, encrypt_data, decrypt_data, key

# Function to collect user input for health records
def collect_health_input():
    # astronaut_id will be assigned via login
    weight = input("Enter Weight: ")
    temperature = input("Enter Temperature (Celcius): ")
    symptoms = input("Enter Symptoms (if any): ")
    radiation_levels = input("Enter Radiation Levels (mSv): ")
    blood_pressure = input("Enter Blood Pressure: ")
    record_date = input("Enter Record Date (YYYY-MM-DD): ")

    return weight, temperature, symptoms, radiation_levels, blood_pressure, record_date

# Add records to database
def add_health_record(key, astronaut_id, weight, temperature, symptoms, radiation_levels, blood_pressure, record_date):
    # Encrypt input
    encrypted_weight = encrypt_data(key, weight)
    encrypted_temperature = encrypt_data(key, temperature)
    encrypted_symptoms = encrypt_data(key, symptoms)
    encrypted_radiation_levels = encrypt_data(key, radiation_levels)
    encrypted_blood_pressure = encrypt_data(key, blood_pressure)

    # Connect to the database
    connect = sqlite3.connect('data/securespace.db')
    cursor = connect.cursor()
    # Insert the new record into the table
    cursor.execute('''
        INSERT INTO health_records (astronaut_id, weight, temperature, symptoms, radiation_levels, blood_pressure, record_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (astronaut_id, encrypted_weight, encrypted_temperature, encrypted_symptoms, encrypted_radiation_levels, encrypted_blood_pressure, record_date))

    # Commit changes and close the connection
    connect.commit()
    connect.close()

    print("\nRecord added successfully!\n")

# Retrieve user id based on username
def get_id_by_username(username):
    connect = sqlite3.connect("data/securespace.db")
    cursor = connect.cursor()

    # Select the id from the database
    cursor.execute('SELECT user_id FROM user_records WHERE username = ?', (username,))
    result = cursor.fetchone()
    connect.close()

    if result:
        return result[0]
    else:
        return None

# Retrieve records by astronaut_id
def retrieve_records(astronaut_id):
    connect = sqlite3.connect("data/securespace.db")
    cursor = connect.cursor()

    # Search for all records with matching astronaut_id
    cursor.execute('SELECT record_id, record_date FROM health_records WHERE astronaut_id = ?', (astronaut_id,))
    records = cursor.fetchall()
    connect.close()

    if records:
        for record in records:
            record_id, record_date = record
            print(f"\nRecord ID: {record_id} - Record Date: {record_date}")
    else:
        print("\nNo records found for this astronaut.")


# Retrieves record based on record_id
def retrieve_record_details(astronaut_id, record_id):
    connect = sqlite3.connect('data/securespace.db')
    cursor = connect.cursor()

    # Select the record
    cursor.execute('SELECT * FROM health_records WHERE record_id = ? AND astronaut_id = ?', (record_id, astronaut_id))
    record = cursor.fetchone()
    connect.close()

    if record:
        decrypted_weight = decrypt_data(key, record[2])
        decrypted_temperature = decrypt_data(key, record[3])
        decrypted_symptoms = decrypt_data(key, record[4])
        decrypted_radiation_levels = decrypt_data(key, record[5])
        decrypted_blood_pressure = decrypt_data(key, record[6])

        print("\nRecord Details:")
        print("--------------")
        print(f"Record ID: {record[0]}")
        print(f"Astronaut ID: {record[1]}")
        print(f"Weight: {decrypted_weight}")
        print(f"Temperature: {decrypted_temperature}")
        print(f"Symptoms: {decrypted_symptoms}")
        print(f"Radiation Levels: {decrypted_radiation_levels}")
        print(f"Blood Pressure: {decrypted_blood_pressure}")
        print(f"Record Date: {record[7]}\n")
    else:
        print("No record found for this record ID.\n")

# Deletes a record from the database based on record_id
def delete_record(astronaut_id, record_id):
    connect = sqlite3.connect('data/securespace.db')
    cursor = connect.cursor()

    # Check if the record belongs to the astronaut based on astronaut_id
    cursor.execute('SELECT * FROM health_records WHERE record_id = ? AND astronaut_id = ?', (record_id, astronaut_id))
    record = cursor.fetchone()

    if record:
        answer = input("Are you sure you want to delete this record? (Y/N): ")
        result = are_you_sure(answer)
        if result == True:
            cursor.execute('DELETE FROM health_records WHERE record_id = ?', (record_id,))
            connect.commit()
            print("Record deleted successfully!\n")
        elif result == False:
            print("Record was not deleted!\n")
        else:
            pass
    else:
        print("Record not found. Please try again.")
    connect.close()