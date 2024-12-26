# aka变种维吉尼亚
import beaufort
from itertools import permutations
def xor_decrypt(ciphertext, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))

ciphertext = bytes.fromhex('1f1a100d1e5c504d1e425d10424e561e0a575e5314570b4557050a584c12545b421b50584344524e5312').decode()
encrypted_key = 'rhiknfxeuyhlcresrvblabmmdppntznqzwqijjnvgo'
iv = 'crypt'

# Decrypt the key，遍历可能的iv
permutations = [''.join(p) for p in permutations(iv)]
for perm in permutations:
    print(perm)
    key = beaufort.beaufort_decipher(encrypted_key,perm)
    key = key.lower()
    # Decrypt the ciphertext
    flag = xor_decrypt(ciphertext, key)
    print(flag)