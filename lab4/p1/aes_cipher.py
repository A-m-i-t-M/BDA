from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC)
        iv = cipher.iv
        ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
        return binascii.hexlify(iv).decode(), binascii.hexlify(ciphertext).decode()

    def decrypt(self, iv_hex, ciphertext_hex):
        iv = binascii.unhexlify(iv_hex)
        ciphertext = binascii.unhexlify(ciphertext_hex)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_data.decode()