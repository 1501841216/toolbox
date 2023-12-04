import os
import re
import rsa
import gmpy2
import requests
import numpy as np
from functools import reduce
from Crypto.Util.number import long_to_bytes, bytes_to_long
import libnum



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

def euler_phi(n):
    result = n   # 初始化结果为n
    p = 2
    while(p * p <= n):
        if (n % p == 0):
            while (n % p == 0):
                n //= p
            result -= result // p
        p += 1
    if (n > 1):     # n为质数
        result -= result // n
    return result

def pqe_4_d(p, q, e):
    phi = (p-1)*(q-1)
    d = gmpy2.invert(e, phi)

    # return long_to_bytes(d)
    return d

# 用于phi过大
def manual_invert(e, phi):
    d = 0
    for k in range(1, 100000):
        if (phi*k+1)%e == 0:
            d = (phi*k+1)//e
    print(d)

    return d

def ndc_4_m(n, d, c):
    h = hex(gmpy2.powmod(c, d, n))[2:]
    if len(h) % 2 == 1:
        h = '0' + h
    s = long_to_bytes(int(h, 16))
    print(s)

    return s

def nec_4_m(n,e,c):
    p,q = query_factors(n)
    d = pqe_4_d(p,q,e)
    s = ndc_4_m(n, d, c)

    return s

def pqec_4_m(p,q,e,c):
    d = pqe_4_d(p,q,e)
    print(d)
    s = ndc_4_m(p * q, d, c)

    return s

# def verify(e,n_A, d_A, data, n_B, d_B, sig):
#     a1 = gmpy2.powmod(sig, e, n_A)
#     a2 = gmpy2.powmod(data, d_A, n_B)
#     print(a1)
#     print(a2)
#
#     return a1, a2

def verify(rsa1, rsa2, data, sig):
    assert (rsa1.e == rsa2.e)
    a1 = gmpy2.powmod(sig, rsa1.e, rsa1.n)
    a2 = gmpy2.powmod(data, rsa2.d, rsa2.n)
    print(long_to_bytes(a1))
    print(long_to_bytes(a2))

    return long_to_bytes(a1), long_to_bytes(a2)

def pem(home, pubkey_file, enc_file):
    # 获取公钥信息
    ret = os.popen('openssl rsa -pubin -text -modulus -in ' + home + pubkey_file).readlines()
    print(ret)
    print(type(ret))
    # 正则读取ret中exponent所在的第五列，为列表，取第一个元素，为字符串
    # ['RSA Public-Key: (256 bit)\n', 'Modulus:\n', '    00:c2:63:6a:e5:c3:d8:e4:3f:fb:97:ab:09:02:8f:\n',
    #  '    1a:ac:6c:0b:f6:cd:3d:70:eb:ca:28:1b:ff:e9:7f:\n', '    be:30:dd\n', 'Exponent: 65537 (0x10001)\n',
    e = int(re.findall(r"Exponent: (.*) \(", list(filter(lambda item: item.startswith("Exponent"), ret))[0])[0])
    print(e)
    # 将modulus的十六进制转化为十进制
    n = int(re.findall(r"Modulus=(.*)\n", list(filter(lambda item: item.startswith("Modulus="), ret))[0])[0], 16)
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

# 共模攻击 使用不同的e、相同的n对相同的m进行多次加密
def comomic_attack(n, e1,e2, c1,c2):
    s = gmpy2.gcdext(e1, e2)
    print(s)
    s1 = s[1]
    s2 = s[2]
    # 求模反元素
    if s1 < 0:
        s1 = -s1
        c1 = gmpy2.invert(c1, n)

    elif s2<0:
        s2 = -s2
        c2 = gmpy2.invert(c2, n)
        # c2 = manual_invert(c2, n)
    m = pow(c1, s1, n)*pow(c2, s2, n)%n
    print( '[-]m is:',long_to_bytes(m))

# 模不互素攻击
def Modules_not_coprime(n1,n2,c1,c2,e):
    p12 = gmpy2.gcd(n1, n2)
    assert (p12 != 1)
    # print('n1',n1)
    # print('n2',n2)
    q1 = n1 // p12
    q2 = n2 // p12
    # print('p12',p12,
    #       '\nq1',q1,
    #       '\nq2',q2)
    m1 = pqec_4_m(p12,q1,e,c1)
    m2 = pqec_4_m(p12,q2,e,c2)

    print(m1.decode() + m2.decode())

# n = '88503001447845031603457048661635807319447136634748350130947825183012205093541'
# queryFactors(n)

if __name__ == '__main__':
    # pem("D:/CTF/crypto/547de1d50b95473184cd5bf59b019ae8/", "pubkey.pem", "flag.enc")

    # pem("D:/CTF/crypto/547de1d50b95473184cd5bf59b019ae8/", "pubkey.pem", "flag.enc")
    # pem("E:\\CTF\\CTFQD\\Crypto\\547de1d50b95473184cd5bf59b019ae8\\", "pubkey.pem", "flag.enc")

    # NO.GFSJ0442 cr3
    # p = 0xa6055ec186de51800ddd6fcbf0192384ff42d707a55f57af4fcfb0d1dc7bd97055e8275cd4b78ec63c5d592f567c66393a061324aa2e6a8d8fc2a910cbee1ed9
    # q = 0xfa0f9463ea0a93b929c099320d31c277e0b0dbc65b189ed76124f5a1218f5d91fd0102a4c8de11f28be5e4d0ae91ab319f4537e97ed74bc663e972a4a9119307
    # e = 0x6d1fdab4ce3217b3fc32c9ed480a31d067fd57d93a9ab52b472dc393ab7852fbcb11abbebfd6aaae8032db1316dc22d3f7c3d631e24df13ef23d3b381a1c3e04abcc745d402ee3a031ac2718fae63b240837b4f657f29ca4702da9af22a3a019d68904a969ddb01bcf941df70af042f4fae5cbeb9c2151b324f387e525094c41
    # c = 0x7fe1a4f743675d1987d25d38111fae0f78bbea6852cba5beda47db76d119a3efe24cb04b9449f53becd43b0b46e269826a983f832abb53b7a7e24a43ad15378344ed5c20f51e268186d24c76050c1e73647523bd5f91d9b6ad3e86bbf9126588b1dee21e6997372e36c3e74284734748891829665086e0dc523ed23c386bb520
    # d = pqe_4_d(p, q, e)
    # print(d)
    # n = p*q
    # s = enc(n, d, c)
    # print(s)

    # NO.GFSJ0751 best_rsa
    # home = 'E:\\CTF\\CTFQD\\Crypto\\c2d6e7158d7b4cd6a747774f0bdc5f72\\'
    #
    # e1 = 117
    # e2 = 65537
    # n = 13060424286033164731705267935214411273739909173486948413518022752305313862238166593214772698793487761875251030423516993519714215306808677724104692474199215119387725741906071553437840256786220484582884693286140537492541093086953005486704542435188521724013251087887351409946184501295224744819621937322469140771245380081663560150133162692174498642474588168444167533621259824640599530052827878558481036155222733986179487577693360697390152370901746112653758338456083440878726007229307830037808681050302990411238666727608253452573696904083133866093791985565118032742893247076947480766837941319251901579605233916076425572961
    # f1 = open(home + 'cipher1.txt','rb')
    # c1 = bytes_to_long(f1.read())
    # f2 = open(home + 'cipher2.txt','rb')
    # c2 = bytes_to_long(f2.read())
    # comomic_attack(n,e1,e2,c1,c2)

    # NO.GFSJ0753 RSA_gcd
    home = 'E:\\CTF\\CTFQD\\Crypto\\f1217fd42e8b43558077180e98c757d7\\attachment\\'
    l1 = open(home + 'attach1.txt', 'r').readlines()
    e = int(l1[1][2:8])
    print(e)
    n1 = int(l1[0][2:])
    c1 = int(l1[3][2:])
    l2 = open(home + 'attach2.txt', 'r').readlines()
    n2 = int(l2[0][2:])
    c2 = int(l2[3][2:])
    Modules_not_coprime(n1,n2,c1,c2,e)