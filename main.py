from cryptography.fernet import Fernet

# 🔑 Step 1: Generate a key (Do this once and save the key securely)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# 🔐 Step 2: Load the saved key
def load_key():
    return open("secret.key", "rb").read()

# 🔏 Step 3: Encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted

# 🔓 Step 4: Decrypt the encrypted password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return decrypted

# ----------------------------
# 🚀 Main Program
# ----------------------------
if __name__ == "__main__":
    # ✅ Run this ONCE to generate the key file (uncomment below line the first time)
    # generate_key()

    # Load the existing key
    key = load_key()

    # Password to encrypt
    password = "MySecretPassword123"

    # Encrypt the password
    encrypted = encrypt_password(password, key)
    print(f"🔐 Encrypted Password: {encrypted}")

    # Decrypt the password
    decrypted = decrypt_password(encrypted, key)
    print(f"🔓 Decrypted Password: {decrypted}")