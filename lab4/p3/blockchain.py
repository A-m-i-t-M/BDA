import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = {
            "index": 0,
            "transaction": "Genesis Block",
            "iv": "",
            "previous_hash": "0",
            "hash": self.hash_block("Genesis Block", "", "0")
        }
        self.chain.append(genesis_block)

    def hash_block(self, transaction, iv, previous_hash):
        block_content = f"{transaction}{iv}{previous_hash}".encode()
        return hashlib.sha256(block_content).hexdigest()

    def add_transaction(self, encrypted_transaction, iv=""):
        previous_hash = self.chain[-1]["hash"]
        new_block = {
            "index": len(self.chain),
            "transaction": encrypted_transaction,
            "iv": iv,  # Not used in AES-ECB mode
            "previous_hash": previous_hash,
            "hash": self.hash_block(encrypted_transaction, iv, previous_hash)
        }
        self.chain.append(new_block)

    def get_chain(self):
        return self.chain