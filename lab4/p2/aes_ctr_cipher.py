from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii
import os

class AESCTRCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        nonce = os.urandom(8)  
        ctr = Counter.new(64, prefix=nonce)
        cipher = AES.new(self.key, AES.MODE_CTR, counter=ctr)
        ciphertext = cipher.encrypt(data.encode())
        return binascii.hexlify(nonce).decode(), binascii.hexlify(ciphertext).decode()

    def decrypt(self, nonce_hex, ciphertext_hex):
        nonce = binascii.unhexlify(nonce_hex)
        ctr = Counter.new(64, prefix=nonce)
        cipher = AES.new(self.key, AES.MODE_CTR, counter=ctr)
        decrypted_data = cipher.decrypt(binascii.unhexlify(ciphertext_hex))
        return decrypted_data.decode()