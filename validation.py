from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()

# Function to validate integers
def validate_integer(variable):
    try:
        int(variable)
        return True
    except TypeError:
        return False

def are_you_sure(answer):
    if answer == "Yes" or answer == "Y" or answer == "yes" or answer == "y":
        return True
    elif answer == "No" or answer == "N" or answer == "no" or answer == "n":
        return False
    else:
        print("Invalid answer. Try again.")
        are_you_sure(answer)

def encrypt_data(key, data):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

def decrypt_data(key, data):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypt_data).decode()
    return decrypted_data

