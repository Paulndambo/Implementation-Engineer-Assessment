import hashlib


def generate_hash_sha256(data):
    hashed = hashlib.sha256(data.encode()).hexdigest()
    return hashed

data = "Hello, World!"
hashed_sha256 = generate_hash_sha256(data)
print(f"SHA-256 Hash: {hashed_sha256}")
