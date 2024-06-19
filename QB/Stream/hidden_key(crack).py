from Crypto.Util.number import bytes_to_long,long_to_bytes
import random
import hashlib

out = 2669175714787937
m = [140, 96, 112, 178, 38, 180, 158, 240, 179, 202, 251, 138, 188, 185, 23, 67, 163, 22, 150, 18, 143, 212, 93, 87, 209, 139, 92, 252, 55, 137, 6, 231, 105, 12, 65, 59, 223, 25, 179, 101, 19, 215]
key = []


def rand(rng):
    return rng - random.randrange(rng)

print(bin(out))
out = out << 12
print(bin(out))

bout = long_to_bytes(out)


for i in bout:
    key.append(i)
print(key)

flag = []
for k in range(2**12):
    tip = 1
    out_guess = out ^ k
    print(bin(out_guess))
    key2 = long_to_bytes(out_guess)
    # print(key2)
    random.seed(int(hashlib.md5(key2).hexdigest(), 16))
    for i in range(len(m)):
        rand(256)
        xor = m[i] ^ rand(256)
        flag.append(chr(xor))
    if 'flag' in ''.join(flag):
        print(''.join(flag))
        break
