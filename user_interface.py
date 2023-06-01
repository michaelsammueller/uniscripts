import sqlite3

# Imports from other files
from login import collect_user_input, register, login
from edit_data import collect_health_input, add_health_record
from edit_data import get_id_by_username, retrieve_records, retrieve_record_details, delete_record
from validation import validate_integer, key

connect = sqlite3.connect('data/securespace.db')

# User Interface
print('''
███████ ████████  █████  ██████        ███    ███ ███████ ██████  
██         ██    ██   ██ ██   ██       ████  ████ ██      ██   ██ 
███████    ██    ███████ ██████  █████ ██ ████ ██ █████   ██   ██ 
     ██    ██    ██   ██ ██   ██       ██  ██  ██ ██      ██   ██ 
███████    ██    ██   ██ ██   ██       ██      ██ ███████ ██████                                                                                                                                                                                                                                                                                                                 
------------------------------------------------------------------
********************* CREATED BY SECURESPACE *********************
------------------------------------------------------------------
''')

def records_menu(astronaut_id):
    while True:
        print("\n1. View Record")
        print("2. Delete Record")
        print("3. Go back\n")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            record_id = input("Record ID: ")
            valid = validate_integer(record_id)
            if valid == True:
                retrieve_record_details(astronaut_id, record_id)
                break
            else:
                print(f"{record_id} is not a valid record ID.\n")
        elif choice == '2':
            record_id = input("Record ID: ")
            valid = validate_integer(record_id)
            if valid == True:
                delete_record(astronaut_id, record_id)
                break
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


def user_menu(username):
    print(f"""
    -------------------------
    Welcome, {username}!
    -------------------------\n""")
    while True:
        print("1. Add Health Record")
        print("2. View Health Records")
        print("3. Log out\n")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            weight, temperature, symptoms, radiation_levels, blood_pressure, record_date = collect_health_input()
            astronaut_id = get_id_by_username(username)
            add_health_record(key, astronaut_id, weight, temperature, symptoms, radiation_levels, blood_pressure, record_date)
        elif choice == '2':
            astronaut_id = get_id_by_username(username)
            retrieve_records(astronaut_id)
            records_menu(astronaut_id)
        elif choice == '3':
            print("Logging out...\n")
            break
        else:
            print("Invalid choice.\n")


def main_menu():
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit\n")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            username, password = collect_user_input()
            if login(username, password):
                user_menu(username)
        elif choice == '2':
            username, password = collect_user_input()
            register(username, password)
        elif choice == '3':
            print("Exiting...\n")
            break
        else:
            print("Invalid choice.\n")

main_menu()