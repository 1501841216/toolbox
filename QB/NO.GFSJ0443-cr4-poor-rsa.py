import base64

import RSA
import rsa
import os
import re
import gmpy2

home = "D:\\CTF\\crypto\\bf930316910b451c94c41ce8a9d851a8\\"
pubkey_file = 'publickey.pem'
enc_file = "test"


# 获取公钥信息
ret = os.popen('openssl rsa -pubin -text -modulus -in ' + home + pubkey_file).readlines()
print(ret)
print(type(ret))
# 正则读取ret中exponent所在的第五列，为列表，取第一个元素，为字符串
# ['RSA Public-Key: (256 bit)\n', 'Modulus:\n', '    00:c2:63:6a:e5:c3:d8:e4:3f:fb:97:ab:09:02:8f:\n',
#  '    1a:ac:6c:0b:f6:cd:3d:70:eb:ca:28:1b:ff:e9:7f:\n', '    be:30:dd\n', 'Exponent: 65537 (0x10001)\n',
e = int(re.findall(r"Exponent: (.*) \(", ret[6])[0])
print(e)
# 将modulus的十六进制转化为十进制
n = int(re.findall(r"Modulus=(.*)\n", ret[7])[0], 16)
print(n)

# 分解n， 获取d，制造私钥
p, q = RSA.query_factors(n)
print(p, q)
fn = (p - 1) * (q - 1)
d = int(gmpy2.invert(e, fn))
key = rsa.PrivateKey(n, e, d, p, q)

# 解密，以二进制读模式读取密文
with open(home + enc_file, 'rb') as f:
    # f：公钥加密的结果， key：私钥
    f = f.read()
    f = base64.b64decode(f)
    print(rsa.decrypt(f, key))