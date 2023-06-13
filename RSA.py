import gmpy2
import requests
from Crypto.Util.number import long_to_bytes,bytes_to_long

def queryFactors(n):
    s = []
    url = 'http://factordb.com/api?query=' + str(n)
    r = requests.get(url)
    factors = r.json()['factors']
    for f in factors:
        for i in range(f[1]):
            s.append(int(f[0]))
    return s

def pqe_4_d(p,q,e):
    phi = (p-1)*(q-1)
    d = gmpy2.invert(e,phi)

    # return long_to_bytes(d)
    return d

def enc(e,n,c):

    print('a')

n = '88503001447845031603457048661635807319447136634748350130947825183012205093541'
queryFactors(n)