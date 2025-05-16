import re  # Import the regex module

# Function to check if an email is valid
def is_valid_email(email):
    # Define a regex pattern for a valid email (username@domain.com)
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # Explanation of the pattern:
    # ^           → start of string
    # [\w\.-]+    → one or more word characters (a-z, A-Z, 0-9, _) or . or -
    # @           → literal @ symbol
    # [\w\.-]+    → one or more word characters (domain part)
    # \.          → a literal dot
    # \w+         → one or more word characters for the domain extension
    # $           → end of string

    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True  # It's a valid email format
    else:
        return False  # It's not valid

# ---------- Test the function ----------
print(is_valid_email("user@domain.com"))   # Output: True
print(is_valid_email("user@domain"))       # Output: False
print(is_valid_email("user.name@domain.org"))  # Output: True
print(is_valid_email("user@.com"))         # Output: False
