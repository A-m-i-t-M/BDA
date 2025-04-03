from blockchain import Blockchain
from aes_standard_cipher import AESStandardCipher
from utils import generate_key
import json

# Generate AES key
key = generate_key()

# Initialize AES Standard Cipher
cipher = AESStandardCipher(key)

# Initialize Blockchain
blockchain = Blockchain()

def menu():
    while True:
        print("\n==== Blockchain AES Standard (ECB) Encryption ====")
        print("1. Add a new encrypted transaction")
        print("2. View Blockchain")
        print("3. Decrypt a transaction")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            transaction_data = input("Enter transaction (e.g., 'Alice → Bob: $100'): ")
            encrypted_transaction = cipher.encrypt(transaction_data)
            blockchain.add_transaction(encrypted_transaction)
            print("\nTransaction encrypted and added to the blockchain!")

        elif choice == "2":
            print("\nBlockchain:")
            for block in blockchain.get_chain():
                print(json.dumps(block, indent=4))

        elif choice == "3":
            index = int(input("\nEnter the block index to decrypt: "))
            if 0 < index < len(blockchain.get_chain()):
                block = blockchain.get_chain()[index]
                decrypted_transaction = cipher.decrypt(block["transaction"])
                print("\nDecrypted Transaction:", decrypted_transaction)
            else:
                print("Invalid block index!")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
