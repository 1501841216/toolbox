# -*- coding: utf-8 -*-
import binascii
from gmssl import sm4
from Crypto.Util.number import long_to_bytes, bytes_to_long

def encode(key, data):
    sm4_a = sm4.CryptSM4()
    sm4_a.set_key(key.encode(), sm4.SM4_ENCRYPT)
    ciphertext = sm4_a.crypt_ecb(str(data).encode()).hex()
    return ciphertext

def decode(key, ciphertext):
    sm4_b = sm4.CryptSM4()
    sm4_b.set_key(key.encode(), sm4.SM4_DECRYPT)
    data = sm4_b.crypt_ecb(long_to_bytes(ciphertext))
    return data

if __name__ == '__main__':
    l = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','f']
    for i in l:
        for n in l:
            for m in l:
                for j in l:
                    key = f'4765{i}df{n}0170{m}44{j}'
                    ciphertext = 0xc49f4552b22f27969c07d9371d1aa093b54f97ccd44261a5fc92cd3461a38d68d20218a51686a3f9d0cc50679e36cd4f
                    text = decode(key,ciphertext)
                    if b'flag{' in text:
                        print(text)

