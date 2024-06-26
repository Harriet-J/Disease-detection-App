import bcrypt
import pickle
from pathlib import Path

# List of plain-text passwords
passwords = ["password1", "password2"]

# Function to hash passwords
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

# Hash the passwords
hashed_passwords = [hash_password(password) for password in passwords]

# Save hashed passwords to a file
file_path = Path(__file__).parent / "hashed.pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
