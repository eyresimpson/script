import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util import Padding


def encrypt_file(file_path, password):
    # Use SHA-256 hash of the password as the encryption key
    encryption_key = hashlib.sha256(password.encode()).digest()

    # Generate a random IV
    iv = os.urandom(AES.block_size)

    # Open the file in binary mode
    with open(file_path, 'rb') as binary_file:
        # Read the binary data from the file
        binary_data = binary_file.read()

    # Pad the binary data to be a multiple of the block size
    padded_data = Padding.pad(binary_data, AES.block_size)

    # Create a cipher object and encrypt the data
    cipher = AES.new(encryption_key, AES.MODE_CBC, iv)
    encrypted_data = iv + cipher.encrypt(padded_data)

    # Write the encrypted data to a new file
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    # Delete the original file
    os.remove(file_path)


def encrypt_folder(folder_path, password):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, password)


encrypt_folder('/path/to/folder', 'secure_password')
