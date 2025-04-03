import hashlib

def generate_key(passphrase = "my_secret_key"):
    return hashlib.sha256(passphrase.encode()).digest()
