# Sample data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Function to add a new user
def add_user(user):
    # Append the new user dictionary to the users list
    users.append(user)
    print("User added successfully.")

# Function to get (Read) a user by ID
def get_user_by_id(user_id):
    # Loop through the list to find the user with matching ID
    for user in users:
        if user["id"] == user_id:
            return user
    return None  # If not found, return None

# Function to update a user's data by ID
def update_user(user_id, updated_data):
    # Go through each user and update if ID matches
    for user in users:
        if user["id"] == user_id:
            user.update(updated_data)  # Update only the provided fields
            print("User updated successfully.")
            return
    print("User not found.")

# Function to delete a user by ID
def delete_user(user_id):
    # Use index to safely remove the item from the list
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            print("User deleted successfully.")
            return
    print("User not found.")

# ---------- Test the functions ----------

# Add a new user
add_user({"id": 3, "name": "Charlie", "email": "charlie@example.com"})

# Read a user
print(get_user_by_id(2))  # Should return Bob's details

# Update a user
update_user(1, {"name": "Alice Smith", "email": "alice.smith@example.com"})

# Delete a user
delete_user(2)

# Final list of users
print("Current users:")
print(users)
