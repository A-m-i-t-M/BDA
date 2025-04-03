from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

class AESStandardCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
        return binascii.hexlify(ciphertext).decode()

    def decrypt(self, ciphertext_hex):
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted_data = unpad(cipher.decrypt(binascii.unhexlify(ciphertext_hex)), AES.block_size)
        return decrypted_data.decode()