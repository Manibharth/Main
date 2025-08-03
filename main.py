from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password, key):
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return decrypted

if __name__ == "__main__":
    key = load_key()
    password = "MySecretPassword123"
    encrypted = encrypt_password(password, key)
    print(f"🔐 Encrypted Password: {encrypted}")
    decrypted = decrypt_password(encrypted, key)
    print(f"🔓 Decrypted Password: {decrypted}")