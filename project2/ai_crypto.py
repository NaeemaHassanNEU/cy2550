import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_file(input_file_path: str, output_file_path: str, key: bytes) -> None:
    """
    Encrypts a file using AES-256-GCM to provide both confidentiality and integrity.
    
    :param input_file_path: Path to the unencrypted source file.
    :param output_file_path: Path where the encrypted output file will be written.
    :param key: A secure, randomly generated 32-byte (256-bit) AES key.
    """
    # 1. Generate a unique 96-bit (12-byte) Initialization Vector (Nonce)
    nonce = os.urandom(12)
    
    # 2. Initialize AES-GCM cipher with the key
    aesgcm = AESGCM(key)
    
    # 3. Read the plaintext file
    with open(input_file_path, 'rb') as f:
        plaintext = f.read()
        
    # 4. Encrypt the data (AES-GCM automatically appends an authentication tag)
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)
    
    # 5. Write the nonce followed by the ciphertext to the output file
    with open(output_file_path, 'wb') as f:
        f.write(nonce + ciphertext)

# Example usage:
if __name__ == "__main__":
    # Generate a cryptographically secure 256-bit key
    symmetric_key = AESGCM.generate_key(bit_length=256)
    
    # Encrypt 'secret.txt' to 'secret.txt.enc'
    # encrypt_file('secret.txt', 'secret.txt.enc', symmetric_key)
