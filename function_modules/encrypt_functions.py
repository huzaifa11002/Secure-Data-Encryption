import json
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64
import hashlib

encrypt_data = "encrypted_data.json"
salt = b'static_salt_value' 

def load_data():
    """ Load JSON data """
    if not os.path.exists(encrypt_data) or os.stat(encrypt_data).st_size == 0:
        return {}
    with open(encrypt_data, "r") as file:
        return json.load(file)

def save_data(data):
    """ Save JSON data """
    with open(encrypt_data, "w") as file:
        json.dump(data,file, indent=4)

def hash_key(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def derive_key(passkey):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(passkey.encode()))

def encrypt(text, passkey):
    KEY = derive_key(passkey)
    cipher = Fernet(KEY)
    return cipher.encrypt(text.encode()).decode()

def decrypt(passkey):
    KEY = derive_key(passkey)
    cipher = Fernet(KEY)

    hashed_key = hash_key(passkey)
    data_file = load_data()

    if hashed_key in data_file:
        encrypted_text = data_file[hashed_key]["encrypted_text"]
        try:
            return cipher.decrypt(encrypted_text.encode()).decode()
        except Exception:
            return None
    else:
        return None