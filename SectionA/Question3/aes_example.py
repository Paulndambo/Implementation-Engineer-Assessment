from base64 import b64decode, b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return b64encode(cipher.nonce + tag + ciphertext).decode()

def decrypt_aes(encrypted_data, key):
    encrypted_data = b64decode(encrypted_data.encode())
    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)
    return decrypted_data.decode()

key = get_random_bytes(16)
data = "Sensitive information"

encrypted_data = encrypt_aes(data, key)
print(f"Encrypted Data: {encrypted_data}")

decrypted_data = decrypt_aes(encrypted_data, key)
print(f"Decrypted Data: {decrypted_data}")
