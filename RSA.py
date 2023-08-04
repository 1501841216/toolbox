import subprocess
import os
import re
import sys
import rsa
import math
import gmpy2
import getopt
import requests
from functools import reduce
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long


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


def enc(n, d, c):
    h = hex(gmpy2.powmod(c, d, n))[2:]
    if len(h) % 2 == 1:
        h = '0' + h
    print(h)
    # s = h.decode('hex')
    print(type(h))
    s = long_to_bytes(int(h, 16))
    return s


def pem(home, pubkey_file, enc_file):
    # 获取公钥信息
    ret = os.popen('openssl rsa -pubin -text -modulus -in ' + home + pubkey_file).readlines()
    print(ret)
    print(type(ret))
    # 正则读取ret中exponent所在的第五列，为列表，取第一个元素，为字符串
    # ['RSA Public-Key: (256 bit)\n', 'Modulus:\n', '    00:c2:63:6a:e5:c3:d8:e4:3f:fb:97:ab:09:02:8f:\n',
    #  '    1a:ac:6c:0b:f6:cd:3d:70:eb:ca:28:1b:ff:e9:7f:\n', '    be:30:dd\n', 'Exponent: 65537 (0x10001)\n',
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

def hastad(n_l, c_l, attack_num):
    sum = 0
    prod = reduce(lambda a, b: a*b, n_l)
    for n_l_i, c_l_i in zip(n_l, c_l):
        p = prod // n_l_i
        sum += c_l_i * gmpy2.invert(p, n_l_i) * p
    m_num = int(sum % prod)
    m = gmpy2.iroot(m_num, attack_num)[0]

    return bytes.fromhex(hex(m)[2:])





# n = '88503001447845031603457048661635807319447136634748350130947825183012205093541'
# queryFactors(n)

if __name__ == '__main__':
    # pem("D:/CTF/crypto/547de1d50b95473184cd5bf59b019ae8/", "pubkey.pem", "flag.enc")

    # pem("D:/CTF/crypto/547de1d50b95473184cd5bf59b019ae8/", "pubkey.pem", "flag.enc")
    pem("E:\\CTF\\CTFQD\\Crypto\\547de1d50b95473184cd5bf59b019ae8\\", "pubkey.pem", "flag.enc")
    # NO.GFSJ0442 cr3
    p = 0xa6055ec186de51800ddd6fcbf0192384ff42d707a55f57af4fcfb0d1dc7bd97055e8275cd4b78ec63c5d592f567c66393a061324aa2e6a8d8fc2a910cbee1ed9
    q = 0xfa0f9463ea0a93b929c099320d31c277e0b0dbc65b189ed76124f5a1218f5d91fd0102a4c8de11f28be5e4d0ae91ab319f4537e97ed74bc663e972a4a9119307
    e = 0x6d1fdab4ce3217b3fc32c9ed480a31d067fd57d93a9ab52b472dc393ab7852fbcb11abbebfd6aaae8032db1316dc22d3f7c3d631e24df13ef23d3b381a1c3e04abcc745d402ee3a031ac2718fae63b240837b4f657f29ca4702da9af22a3a019d68904a969ddb01bcf941df70af042f4fae5cbeb9c2151b324f387e525094c41
    c = 0x7fe1a4f743675d1987d25d38111fae0f78bbea6852cba5beda47db76d119a3efe24cb04b9449f53becd43b0b46e269826a983f832abb53b7a7e24a43ad15378344ed5c20f51e268186d24c76050c1e73647523bd5f91d9b6ad3e86bbf9126588b1dee21e6997372e36c3e74284734748891829665086e0dc523ed23c386bb520
    d = pqe_4_d(p, q, e)
    print(d)
    n = p*q
    s = enc(n, d, c)
    print(s)
