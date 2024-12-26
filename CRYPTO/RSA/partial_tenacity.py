# An RSA without offering e
# partial p and q
# violent attack
# 2024 Cyber Apocalypse

"""
with open('output.txt', 'w') as f:
    f.write(f'n = {cipher.key.n}\n')
    f.write(f'ct = {enc_flag.hex()}\n')
    # 从头开始，每隔一个字符取一次
    f.write(f'p = {str(cipher.key.p)[::2]}\n')
    # 从第二个字符开始，每隔一个字符取一次
    f.write(f'q = {str(cipher.key.q)[1::2]}')
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import *
from math import sqrt


class RSACipher:
    def __init__(self, bits):
        self.key = RSA.generate(bits)
        self.cipher = PKCS1_OAEP.new(self.key)

    def encrypt(self, m):
        return self.cipher.encrypt(m)

    def decrypt(self, c):
        return self.cipher.decrypt(c)


cipher = RSACipher(1024)

n = 118641897764566817417551054135914458085151243893181692085585606712347004549784923154978949512746946759125187896834583143236980760760749398862405478042140850200893707709475167551056980474794729592748211827841494511437980466936302569013868048998752111754493558258605042130232239629213049847684412075111663446003
ct = 0x7f33a035c6390508cee1d0277f4712bf01a01a46677233f16387fae072d07bdee4f535b0bd66efa4f2475dc8515696cbc4bc2280c20c93726212695d770b0a8295e2bacbd6b59487b329cc36a5516567b948fed368bf02c50a39e6549312dc6badfef84d4e30494e9ef0a47bd97305639c875b16306fcd91146d3d126c1ea476
hp = 151441473357136152985216980397525591305875094288738820699069271674022167902643
hq = 15624342005774166525024608067426557093567392652723175301615422384508274269305


# Produce masks for p and q
# according to the length of square root of n
# and the digit feature of p and q given in the problem
def create_masks(primelen):
    pmask = ''.join(['1' if i % 2 == 0 else '0' for i in range(primelen)])
    qmask = ''.join(['1' if i % 2 == 1 else '0' for i in range(primelen)])
    return pmask, qmask


def restore(i, n, know, check, hint):
    msk = 10**(i+1)
    know = 10**i*(hint%10)+know #提取已知位，并恢复
    for d in range(10):
        test = 10**i*d+ check #为未知的位，赋高位，来做检验
        if n%msk  == (know * test)%msk :
            check = test
            hint = hint //10
            return know,check,hint


def factor(n, p, q, hp, hq, pmask, qmask):
    for i in range(len(pmask)):
        if pmask[-i-1] == '1':
            # crack q
            p,q,hp = restore(i,n,p,q,hp)
        else:
            # crack p
            q,p,hq = restore(i,n,q,p,hq)
    assert n==p*q
    return p,q


def decrypt(p, q, n, ct):
    e = 0x10001
    d = pow(e, -1, (p-1)*(q-1))
    key = RSA.construct((n, e, d))
    flag = PKCS1_OAEP.new(key).decrypt(ct)
    return flag


ct = long_to_bytes(ct)
pmask, qmask = create_masks(len(str(int(sqrt(n)))))
p,q = factor(n,0,0,hp,hq,pmask,qmask)
print(decrypt(p,q,n,ct))