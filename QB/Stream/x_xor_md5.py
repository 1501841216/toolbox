import binascii
import hashlib
import base
from Crypto.Util.number import long_to_bytes, bytes_to_long

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

file_path = "E:\\CTF\\CTFQD\\Crypto\\6c0c57fa88eb44f3b179a6e9798fc7b6"

with open(file_path,"rb") as f:
    fr = f.read()
    key = binascii.hexlify(fr[80:96])
    print(key)