# Imports
import bcrypt

# Hashes a password
def hash_password(password):
    """Converting user password into another string"""

    # Converts password into bytes
    bytes = password.encode('utf-8')
    
    # Generating salt - random string that is added to the password. Hashing always produces the same output based on the same input
    # meaning that if someone has access to the database, hashing alone can be vulnerable. 
    salt = bcrypt.gensalt()

    # Assembling the hash
    hash = bcrypt.hashpw(bytes, salt)

    return hash

# Confirms user input against stored password
def authenticate(user_password, hashed_password):
    """Authenticates user password"""

    # Converts password into bytes
    bytes = user_password.encode('utf-8')

    # Checks user input against hashed password
    result = bcrypt.checkpw(bytes, hashed_password)

    return result

# Tests
password = "password123"

hash = hash_password(password)
print(hash)

# Test with wrong password
userInput = "password321"

authentication = authenticate(userInput, hash)
print(authentication)

# Test with correct password
userInput = "password123"

authentication = authenticate(userInput, hash)
print(authentication)