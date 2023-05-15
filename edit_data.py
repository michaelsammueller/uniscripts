import sqlite3

# Function to collect user input for health records
def collect_health_input():
    # astronaut_id will be assigned via login
    weight = float(input("Enter Weight: "))
    temperature = float(input("Enter Temperature: "))
    symptoms = input("Enter Symptoms (if any): ")
    radiation_levels = float(input("Enter Radiation Levels: "))
    blood_pressure = input("Enter Blood Pressure: ")
    record_date = input("Enter Record Date (YYYY-MM-DD): ")

    return weight, temperature, symptoms, radiation_levels, blood_pressure, record_date

# Add records to database
def add_health_record(astronaut_id, weight, temperature, symptoms, radiation_levels, blood_pressure, record_date):
    # Connect to the database
    connect = sqlite3.connect('data/astronauts.db')
    cursor = connect.cursor()

    # Insert the new record into the table
    cursor.execute('''
        INSERT INTO health_records (astronaut_id, weight, temperature, symptoms, radiation_levels, blood_pressure, record_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (astronaut_id, weight, temperature, symptoms, radiation_levels, blood_pressure, record_date))

    # Commit changes and close the connection
    connect.commit()
    connect.close()

    print("Record added successfully!")