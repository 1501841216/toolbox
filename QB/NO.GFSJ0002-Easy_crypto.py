import RSA
import gmpy2
from Crypto.Util.number import bytes_to_long

key = 'hello world'
s = []
t = []
j = 0
for i in range(0, 256):
    s.append(i)
print(s)

for i in range(0, 256):
    t.append(key[i % len(key)])
print(t)

for i in range(0, 256):
        j = (j+int(s[i]) + int(ord(t[i]))) % 256
        s[i], s[j] = s[j], s[i]
print(s)


# def encrypt():
#     for m in range(0, 38):
#         i = (i+1)%256
#         j = (j+s[i])%256
#         s[i],s[j] = s[j],s[i]
#         x = (s[i]+s[j]%256)%256
#         flag[m] = flag[m]^s[x]
#     print(flag)

def decrypt(cipher):
    i=0;j=0
    for m in range(0,37):
        i = (i+1)%256
        j = (j+s[i])%256
        s[i],s[j] = s[j],s[i]
        x = (s[i]+(s[j]%256))%256
        cipher[m] = chr(cipher[m]^s[x])
    print(cipher)
    print(''.join(cipher[i] for i in range(0, 37)))

home = 'D:\\CTF\\Crypto\\1f184c58079f435f85e5d450a07046fa\\enc\\'
f = open(home + 'enc.txt','rb')
cipher = []
data = f.read().hex()
print(len(data))

byte_stream = bytes.fromhex(data)

for byte in byte_stream:
    cipher.append(byte)
print(cipher)
decrypt(cipher)




