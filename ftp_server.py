from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from cryptography.fernet import Fernet
import hashlib

# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Function to encrypt a file
def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        encrypted_data = cipher.encrypt(data)
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_path):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path[:-10], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

# Function to calculate hash value of a file
def calculate_hash(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        hash_value = hashlib.sha256(data).hexdigest()
    return hash_value

# Set up FTP server
authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", ".", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()
