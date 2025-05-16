import hashlib

# Dictionary to store username: hashed_password
user_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in user_db:
        return "Error: User already exists"
    hashed_pw = hash_password(password)
    user_db[username] = hashed_pw
    return "Created new user"

def login(username, password):
    hashed_pw = hash_password(password)
    if username in user_db and user_db[username] == hashed_pw:
        return "Login Successful"
    return "Login Failed"

# ----- Test cases -----
print(register("john", "mypassword"))  # Output: Created new user
print(login("john", "mypassword"))     # Output: Login Successful

# Additional test cases
print(register("john", "anotherpass")) # Output: Error: User already exists
print(login("john", "wrongpass"))      # Output: Login Failed
print(login("doe", "any"))             # Output: Login Failed
