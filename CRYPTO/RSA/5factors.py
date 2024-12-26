# GFSJ1117
# fundamental
# RSA 5 specific factors

# import libnum
# from Crypto.Util import number
# from functools import reduce
# from secret import flag
#
# n = 5
# size = 64
# while True:
#     ps = [number.getPrime(size) for _ in range(n)]
#     if len(set(ps)) == n:
#         break
#
# e = 65537
# n = reduce(lambda x, y: x*y, ps)
# m = libnum.s2n(flag)
# c = pow(m, e, n)
#
# print('n = %d' % n)
# print('c = %d' % c)
from gmpy2 import invert

import myRSA
from Crypto.Util.number import long_to_bytes

n = 175797137276517400024170861198192089021253920489351812147043687817076482376379806063372376015921
c = 144009221781172353636339988896910912047726260759108847257566019412382083853598735817869933202168
e = 65537

f = myRSA.query_factors(n)
f1 = f[0]
f2 = f[1]
f3 = f[2]
f4 = f[3]
f5 = f[4]
phi = (f1 - 1) * (f2 - 1) * (f3 - 1) * (f4 - 1) * (f5 - 1)
d = invert(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))


