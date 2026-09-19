import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def encrypt_file(input_file_path: str, output_file_path: str, key: bytes) -> None:
    """
    Encrypts a file securely using AES-256-GCM (Authenticated Encryption).
    
    - Generates a fresh 96-bit (12-byte) random nonce per file.
    - Encrypts plaintext and appends an authentication tag to prevent tampering.
    - Prepends the nonce to the ciphertext for use during decryption.
    """
    if len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes (256 bits) for AES-256.")

    # 1. Generate a cryptographically secure, unpredictable 12-byte nonce (IV)
    nonce = os.urandom(12)
    
    # 2. Initialize AES-GCM cipher mode
    aesgcm = AESGCM(key)
    
    # 3. Read input plaintext
    with open(input_file_path, 'rb') as f_in:
        plaintext = f_in.read()
        
    # 4. Encrypt data and compute authentication tag
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)
    
    # 5. Output [nonce (12 bytes) + ciphertext + tag (16 bytes)]
    with open(output_file_path, 'wb') as f_out:
        f_out.write(nonce + ciphertext)


def decrypt_file(encrypted_file_path: str, output_file_path: str, key: bytes) -> None:
    """
    Decrypts a file encrypted with AES-256-GCM and verifies its authenticity.
    
    - Extracts the 12-byte nonce from the beginning of the file.
    - Decrypts and verifies integrity using AES-GCM (raises InvalidTag on tampering).
    """
    if len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes (256 bits) for AES-256.")

    with open(encrypted_file_path, 'rb') as f_in:
        data = f_in.read()
        
    # Extract the 12-byte nonce from the header
    nonce = data[:12]
    ciphertext = data[12:]
    
    aesgcm = AESGCM(key)
    
    # Decrypt and authenticate (raises cryptography.exceptions.InvalidTag if corrupted/tampered)
    plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data=None)
    
    with open(output_file_path, 'wb') as f_out:
        f_out.write(plaintext)


# --- Round-Trip Verification Test ---
if __name__ == "__main__":
    test_input = "test_plain.txt"
    test_encrypted = "test_encrypted.bin"
    test_decrypted = "test_decrypted.txt"
    
    # Create test plaintext file
    with open(test_input, "w") as f:
        f.write("CY2550 Project 2 - Authenticated Encryption Test Pass")
        
    # Generate a secure 256-bit symmetric key
    key = AESGCM.generate_key(bit_length=256)
    
    # Test encryption and decryption round-trip
    encrypt_file(test_input, test_encrypted, key)
    decrypt_file(test_encrypted, test_decrypted, key)
    
    # Verify contents match
    with open(test_input, "rb") as original, open(test_decrypted, "rb") as recovered:
        assert original.read() == recovered.read(), "Round-trip failed."
        
    print("Encryption/Decryption round-trip successful. Files match perfectly.")
