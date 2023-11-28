import RSA
import gmpy2

key = 'hello world'
s = []
t = []
flag = ''
for i in range(0, 256):
    s += str(i)
print(s)

for i in range(0, 256):
    t += key[i % len(key)]
print(t)

def encrypt():
    for i in range(0,256):
        j = (j+s[i]+t[i])%256
        s[i], s[j] = s[j], s[i]

    for m in range(0,37):
        i = (i+1)%256
        j = (j+s[i])%256
        s[i],s[j] = s[j],s[i]
        x = (s[i]+s[j]%256)%256
        flag[m] = flag[m]**s[x]
    print(flag)

def decrypt(cipher):
    for m in range(0,37):
        i = (i-1)%256
        j = (j-s[i])%256
        s[i],s[j] = s[j],s[i]
        x = (s[i]-s[j]%256)%256
        inv_sx = gmpy2.invert(s[x],RSA.euler_phi(37))
        cipher [m] = cipher[m]**inv_sx

home = 'E:\\CTF\\CTFQD\\Crypto\\1f184c58079f435f85e5d450a07046fa\\enc\\'
f = open(home + 'enc.txt','rb')
cipher = f.read()
decrypt(cipher)





