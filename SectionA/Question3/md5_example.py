import hashlib


def generate_hash_md5(data):
    hashed = hashlib.md5(data.encode()).hexdigest()
    return hashed

data = "Hello, World!"
hashed_md5 = generate_hash_md5(data)
print(f"MD5 Hash: {hashed_md5}")
