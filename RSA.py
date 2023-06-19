import subprocess
import os
import re
import sys
import rsa
import math
import gmpy2
import getopt
import requests
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA


def query_factors(n):
    s = []
    url = 'http://factordb.com/api?query=' + str(n)
    r = requests.get(url)
    factors = r.json()['factors']
    for f in factors:
        for i in range(f[1]):
            s.append(int(f[0]))
    # p,q = s, s = [p, q]
    return s


def pqe_4_d(p, q, e):
    phi = (p-1)*(q-1)
    d = gmpy2.invert(e, phi)

    # return long_to_bytes(d)
    return d


def enc(e, n, c):

    print('a')


def pem(home, pubkey_file, enc_file):
    # 获取公钥信息
    ret = os.popen('openssl rsa -pubin -text -modulus -in ' + home + pubkey_file).readlines()
    print(ret)
    # 正则读取ret中exponent所在的第五列，为列表，取第一个元素，为字符串
    e = int(re.findall(r"Exponent: (.*) \(", ret[5])[0])
    print(e)
    # 将modulus的十六进制转化为十进制
    n = int(re.findall(r"Modulus=(.*)\n", ret[6])[0], 16)
    print(n)

    # 分解n， 获取d，制造私钥
    p, q = query_factors(n)
    print(p, q)
    fn = (p-1)*(q-1)
    d = int(gmpy2.invert(e, fn))
    key = rsa.PrivateKey(n, e, d, p, q)

    # 解密，以二进制读模式读取密文
    with open(home + enc_file, 'rb') as f:
        # f：公钥加密的结果， key：私钥
        f = f.read()
        print(rsa.decrypt(f, key))


# n = '88503001447845031603457048661635807319447136634748350130947825183012205093541'
# queryFactors(n)


pem("D:/CTF/crypto/547de1d50b95473184cd5bf59b019ae8/", "pubkey.pem", "flag.enc")
