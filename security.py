from cryptography.fernet import Fernet

# This key should be securely stored and managed
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()
