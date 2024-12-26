# 2024baseCTF
from Crypto.Util.number import *
import random
import myRSA
import gmpy2

n, c, e = 0, 0, 0
primes = []
with open("F:\\CTF\\CTFQD\\games\\2024BaseCTF\\random_primes\\output.txt") as f:
    exec(f.read())
original_n = n
print(e)

def gen_n():
    primes = [getPrime(128) for _ in range(256)]
    n = 1
    for i in range(100):
        n *= primes[random.randint(0, 127)]
    return primes, n

def find_all_factors(n, primes):
    count= 0
    factors = []
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n //= p
            count += 1
    print(count)
    return factors


def decrypt(c, factors, e, original_n):
    phi = 1
    print(len(factors))
    print(original_n)
    for i in factors:
        phi *= (i - 1)
    d = gmpy2.invert(e, phi)
    m = pow(c, d, original_n)
    return long_to_bytes(m)

def decrypt2(c, factors, e, original_n):
    phi = 1
    unique_factors = list(set(factors))  # remove duplicates
    for i in unique_factors:
        phi *= (i - 1) * (i ** (factors.count(i) - 1))
    d = gmpy2.invert(e, phi)
    if d == 0:
        print("No modular multiplicative inverse exists")
        return None
    m = pow(c, d, original_n)
    return long_to_bytes(m)

# original_n = n
# factors = find_all_factors(n, primes)
# print("Factors: ", factors)
# print(decrypt2(c, factors, e, original_n))

n = 27097913523613788589653007238329449111398611308532560896913882358010020680431
e = 65537
c = 2099316313813295654473458261289278532565224109996926385717322389081272868827
factors = [13143406850175765791,12727486165623275281,12727486165623275281,12727486165623275281]
print(decrypt2(c,factors,e,n))
