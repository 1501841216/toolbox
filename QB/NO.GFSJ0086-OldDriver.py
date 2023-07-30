import os
import re
from functools import reduce
import gmpy2
from Crypto.Util.number import long_to_bytes, bytes_to_long
# from RSA import query_factors

the_dir = 'E:\\CTF\\CTFQD\\Crypto\\4981449e0af24b10a4125ee647270fe3'
f = open(the_dir + "\\enc.txt", 'r', )
n_list = []
c_list = []
for line in f:
    print("-----")
    c = re.findall(r"\"c\": (.*), \"e", line)[0]
    e = re.findall(r"\"e\": (.*), \"n", line)[0]
    n = re.findall(r"\"n\": (.*)}", line)[0]
    n_list.append(n)
    c_list.append(c)

def chinese_remainder(n, a):#
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * gmpy2.invert(p, n_i) * p
    return int(sum % prod)

m_9=chinese_remainder(n_list[:5],c_list[:5])
m=gmpy2.iroot(m_9,9)[0]
print(bytes.fromhex(hex(m)[2:]))