from cryptography.fernet import Fernet

# Generate a random encryption key
encryption_key = Fernet.generate_key()

print(encryption_key)
