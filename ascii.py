from Crypto.Util.number import long_to_bytes, bytes_to_long
import libnum
import base64
import os


the_dir = 'D:\\CTF\\crypto'
f = open(the_dir + "\\a7cefaacd1684bfdabd71b0e848c3b83.txt", "r")
for line in f:
    b = long_to_bytes(int(line, 16))
    s = libnum.n2s(int(line, 16))
    print(type(s))
    print(s)
    print(s.decode())
    # print(s.replace('\\x', ''))
