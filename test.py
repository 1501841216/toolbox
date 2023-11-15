import hashlib

hashlib.new('md4', "test".encode()).hexdigest()