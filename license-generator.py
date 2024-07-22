import secrets
import string

def generate_key():
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(16))

# Generate a random key
key = generate_key()

# Get user initials
initials = input("User initials: ")

# Ensure the initials are exactly 2 characters long
if len(initials) != 2:
    raise ValueError("User initials must be exactly 2 characters long.")

# Replace first and last characters of key with user initials
key = initials[0] + key[1:15] + initials[1]

# Append key to file
with open('key-list.txt', 'a+') as keyfile:
    keyfile.seek(0)
    content = keyfile.read().strip()

    if content == "":
        keyfile.write(key)
    else:
        keyfile.write(f"\n{key}")

print(f"Generated and saved key: {key}")

