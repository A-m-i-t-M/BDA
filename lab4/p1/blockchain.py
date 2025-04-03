import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_gen()
        return

    def create_gen(self):
        genesis_block = {
                "index" : 0,
                "transaction" : "Genesis Block",
                "iv" : "",
                "previous_hash" : "0",
                "hash" : self.hash("Genesis Block", "", "0")
                }
        self.chain.append(genesis_block)
        return

    def hash(self, transaction, iv, prev_hash):
        block_content = f"{transaction}{iv}{prev_hash}".encode()
        return hashlib.sha256(block_content).hexdigest()

    def add_transaction(self, encrypted_transaction, iv):
        previous_hash = self.chain[-1]["hash"]
        new_block = {
                "index" : len(self.chain),
                "transaction" : encrypted_transaction,
                "iv" : iv,
                "previous_hash" : previous_hash,
                "hash" : self.hash(encrypted_transaction, iv, previous_hash)
                }
        self.chain.append(new_block)
        return

    def get_chain(self):
        return self.chain
