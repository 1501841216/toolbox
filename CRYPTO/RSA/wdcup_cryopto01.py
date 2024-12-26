from sage.all import *
from Crypto.Util.number import *

block_size = 64
rounds = 14

P_permutation = Permutations(list(range(block_size))).random_element()
inverse_P_permutation = [P_permutation.index(i) for i in range(block_size)]

MASK = 0b1110001001111001000110010000100010101111101100101110100001001001
IV = 7

b2i = lambda x: Integer(sum([x[i] * 2**i for i in range(len(x))]))

def pad(x):
    padlen = block_size - len(x) % block_size
    return x + bytes([padlen] * padlen)

def P(x):
    bit_x = x.bits()
    if len(bit_x) < block_size:
        bit_x.extend([0] * (block_size - len(bit_x)))
    bit_x = [bit_x[P_permutation[i]] for i in range(block_size)]
    return b2i(bit_x)

def P_inv(x):
    bit_x = x.bits()
    if len(bit_x) < block_size:
        bit_x.extend([0] * (block_size - len(bit_x)))
    bit_x = [bit_x[inverse_P_permutation[i]] for i in range(block_size)]
    return b2i(bit_x)

def S(x):
    x1 = x
    x2 = x << IV & MASK
    x3 = x << IV & ((1 << block_size) - 1) | MASK
    return x1 ^ x2 ^ x3

def encrypt(message_block, key):
    ret = message_block
    for i in range(rounds):
        ret = P_inv(S(P(ret)) ^ key)
    return ret

from secret import flag
from hashlib import md5

message = pad(flag)
message = [Integer(bytes_to_long(message[i:i+8])) for i in range(0, len(message), 8)]

key = int(md5(flag).hexdigest(), 16) & ((1 << block_size) - 1)

ciphertext = [encrypt(m, key) for m in message]

print(ciphertext)
print(P_permutation)