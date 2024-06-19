from os import urandom
import binascii
from Crypto.Util.number import bytes_to_long

P = 0x10000000000000000000000000000000000000000000000000000000000000425


def process(m, k):
    tmp = m ^ k
    res = 0
    for i in bin(tmp)[2:]:
        res = res << 1
        if (int(i)):
            res = res ^ tmp
        if (res >> 256):
            res = res ^ P
    return res


def keygen(seed):
    key = str2num(urandom(32))
    while True:
        yield key
        key = process(key, seed)



def str2num(s):
    # return int(s.encode('hex'), 16)
    if type(s) == str:
        return int(binascii.hexlify(s.encode()), 16)
    if type(s) == bytes:
        return int(binascii.hexlify(s), 16)


true_secret = open('flag.txt').read()[:32]
assert len(true_secret) == 32
print('flag{%s}' % true_secret)
fake_secret1 = "I_am_not_a_secret_so_you_know_me"
fake_secret2 = "feeddeadbeefcafefeeddeadbeefcafe"
secret = str2num(urandom(32))

generator = keygen(secret)
ctxt1 = hex(str2num(true_secret) ^ generator.next())[2:-1]
ctxt2 = hex(str2num(fake_secret1) ^ generator.next())[2:-1]
ctxt3 = hex(str2num(fake_secret2) ^ generator.next())[2:-1]
f = open('ciphertext', 'w')
f.write(ctxt1+'\n')
f.write(ctxt2+'\n')
f.write(ctxt3+'\n')
f.close()

# f = open('E:\\CTF\\CTFQD\\Crypto\\efed073d048f40119b1e7ec2577910ee\\ciphertext', 'r')
# lines = f.read()
# ctxt1 = lines.split('\n')[0]
# ctxt2 = lines.split('\n')[1]
# ctxt3 = lines.split('\n')[2]
#
# key2 = str2num(fake_secret1) ^ int(ctxt2, 16)
# key3 = str2num(fake_secret2) ^ int(ctxt3, 16)
# print(key2)
# print(key3)
# # print(urandom(32))
# # print(bytes_to_long(urandom(32)))
# # print(len(str(bytes_to_long(urandom(32)))))
# print(len(bin(P)))