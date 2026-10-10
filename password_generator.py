import random
import string

def generate_password(length=10):
    """
    Generates a secure random password containing letters, digits, and punctuation.
    Uses a default length of 10 if no argument is provided.
    """
    # Combine letters, digits, and punctuation characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters based on the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    # Test the function directly when running this script
    print("Default Password (length 10):", generate_password())
    print("Custom Length Password (length 16):", generate_password(16))
