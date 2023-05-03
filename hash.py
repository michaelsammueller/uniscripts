import bcrypt

# To test this function prior to database implementation, this dictionary will act as the database
hashed_users = {'gordon.ramsay': '$2b$12$XoYVPnA2R60I8fBQ2P77su2Sd4x1DMkxodHiGUylje.j/dDNF98Cy', 
                'john.wick': '$2b$12$hSeY5N/C8DzQifNlZRj8VOmMQi.L69Xn3eWDeKVZj37rXvSSM6lTa', 
                'james.bond': '$2b$12$kW4O23Dtm7ozzBNtBJ5W4Oge4bNo90mDimSeAgkgRpxf4wdMmlK8S'}

# Retrieves user password hash from database based on username
def get_password_hash(username):
    """Retrieves password hash for existing users"""
    return hashed_users.get(username)

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

    # Convert bytes hash to a string and return
    return hash.decode('utf-8')

# Confirms user password against stored password hash
def auth_password(password, hash):
    """Authenticates user password"""

    # Converts password into bytes
    bytes = password.encode('utf-8')

    # Convert hash string to bytes before passing to bcrypt.checkpw()
    hash_bytes = hash.encode('utf-8')

    # Checks user input against hashed password
    result = bcrypt.checkpw(bytes, hash_bytes)

    return result

# Authenticates user based on database
def auth_user(username, password):
    """User Authentication"""
    hash = get_password_hash(username)

    if not hash:
        # If no user with this username exists:
        print("Username or Password incorrect!")
        return False
    
    if auth_password(password, hash):
        print("Login successful!")
        return True
    else:
        print("Username or Password incorrect!")
        return False


# Test the authentication function
gordon_authenticate = auth_user('gordon.ramsay', 'lambsauce')
print(gordon_authenticate)
