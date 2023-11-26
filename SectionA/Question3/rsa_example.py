from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

## Commands to generate .pem file
# openssl genpkey -algorithm RSA -out private.pem
# openssl rsa -pubout -in private.pem -out public.pem

def encrypt_rsa(data, public_key_path):
    key = RSA.import_key(open(public_key_path).read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(data.encode())
    return ciphertext

def decrypt_rsa(encrypted_data, private_key_path):
    key = RSA.import_key(open(private_key_path).read())
    cipher = PKCS1_OAEP.new(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()

public_key_path = "public.pem"
private_key_path = "private.pem"
data = "Secure communication"

encrypted_data = encrypt_rsa(data, public_key_path)
print(f"Encrypted Data: {encrypted_data}")

decrypted_data = decrypt_rsa(encrypted_data, private_key_path)
print(f"Decrypted Data: {decrypted_data}")
