import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util import Padding


def decrypt_file(file_path, password):
    # Use SHA-256 hash of the password as the decryption key
    decryption_key = hashlib.sha256(password.encode()).digest()

    # Open the encrypted file in binary mode
    with open(file_path, 'rb') as encrypted_file:
        # Read the encrypted data from the file
        encrypted_data = encrypted_file.read()

    # Extract the IV from the beginning of the encrypted data
    iv = encrypted_data[:AES.block_size]
    encrypted_data = encrypted_data[AES.block_size:]

    # Create a cipher object and decrypt the data
    cipher = AES.new(decryption_key, AES.MODE_CBC, iv)
    padded_data = cipher.decrypt(encrypted_data)

    # Unpad the data
    binary_data = Padding.unpad(padded_data, AES.block_size)

    # Write the binary data to a new file
    decrypted_file_path = file_path[:-len('.encrypted')]
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(binary_data)

    # Delete the encrypted file
    os.remove(file_path)


def decrypt_folder(folder_path, password):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith('.encrypted'):
                decrypt_file(file_path, password)


decrypt_folder('/path/to/folder', 'secure_password')
