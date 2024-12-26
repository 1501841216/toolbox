import myRSA
import os
import re
from Crypto.Util.number import*
from Crypto.PublicKey import RSA

pubkey_file = 'F:\\CTF\\CTFQD\\games\\2024wdcup\\2024wdzq\\crypto\\6ef4da86f05aa837363e1fb2a3cca365\\flag.pem'
def extract_pem(c_file, key_file):
    c = bytes_to_long(open(c_file,'rb').read())
    key = RSA.importKey(open(key_file, 'rb').read())
    n,e=key.n,key.e
    return n,e,c


# ret = open(pubkey_file, 'rb').read()
# print(ret)
# print(bytes_to_long(ret))

ret = os.popen('openssl rsa -pubin -text -modulus -in ' + pubkey_file).readlines()
print(ret)

# 使用正则表达式提取 exponent 和 modulus
e = int(re.findall(r"Exponent: (.*) \(", list(filter(lambda item: item.startswith("Exponent"), ret))[0])[0])
print(e)
n = int(re.findall(r"Modulus=(.*)\n", list(filter(lambda item: item.startswith("Modulus="), ret))[0])[0], 16)
print(n)
# ret = os.popen('openssl rsa -pubin -text -modulus -in ' + pubkey_file).readlines()
# print(ret)
# print(type(ret))
# # 正则读取ret中exponent所在的第五列，为列表，取第一个元素，为字符串
# # ['RSA Public-Key: (256 bit)\n', 'Modulus:\n', '    00:c2:63:6a:e5:c3:d8:e4:3f:fb:97:ab:09:02:8f:\n',
# #  '    1a:ac:6c:0b:f6:cd:3d:70:eb:ca:28:1b:ff:e9:7f:\n', '    be:30:dd\n', 'Exponent: 65537 (0x10001)\n',
# e = int(re.findall(r"Exponent: (.*) \(", list(filter(lambda item: item.startswith("Exponent"), ret))[0])[0])
# print(e)
# # 将modulus的十六进制转化为十进制
# n = int(re.findall(r"Modulus=(.*)\n", list(filter(lambda item: item.startswith("Modulus="), ret))[0])[0], 16)
# print(n)