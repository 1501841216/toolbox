# pem reader
# NO.SJ0172-wtc_rsa_bbq
# n+1 is very close to a power of 2
# 见笔记n+1非常整

from Crypto.Util.number import long_to_bytes, bytes_to_long
from math import isqrt


from Crypto.PublicKey import RSA
import myRSA
import base64
MAXLINESIZE = 76 # Excluding the CRLF
MAXBINSIZE = (MAXLINESIZE//4)*3


def extract_pem(c_file, key_file):
    c = bytes_to_long(open(c_file,'rb').read())
    key = RSA.importKey(open(key_file).read())
    n,e=key.n,key.e
    return n,e,c


home = 'F:\\CTF\\CTFQD\\Crypto\\82f462a5eb8543899f11b46cbfb4d827\\cry200\\'

n,e,c = extract_pem(home + 'cipher.bin',home + 'key.pem')
print(hex(n))
s = myRSA.query_factors(n)
p = s[0]
q = s[1]
m = myRSA.pqec_4_m(p,q,e,c)
print(m)

# if violence can't crack it, use the square root to find their factors
i = isqrt(n)
p, q = 0, 0
while True:
    if n % i == 0:
        p = i
        q = n // i
        break
    i += 1

print(f"p: {p}, q: {q}")


