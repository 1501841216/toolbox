from Crypto.Util.number import long_to_bytes, bytes_to_long
import libnum
import base64
import os


the_dir = 'D:\\CTF\\crypto'
f = open(the_dir + "\\a7cefaacd1684bfdabd71b0e848c3b83.txt", "r")
for line in f:
    b = long_to_bytes(int(line, 16))
    print(type(b))
    print(b)
    print(b.decode('utf-8', 'ignore'))

# fin = open(the_dir + "\\cipher.txt", 'r')
# fout = open(the_dir + "\\2.zip", "wb")
# base64.decode(fin, fout)
# f.close()
# fout.close()

a = [118, 104, 102, 120, 117, 108, 119, 124, 48, 123, 101, 120]
s = ''
for item in a:
    s += chr(item-3)

print(s)