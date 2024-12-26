from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b

v5 = ["11223344", "55667788", "99AABBCC", "DDEEFF11"]
v6 = ["94B1F1E7", "21D5D352", "5247793D", "040D1C97", "F36E7F74", "9C53F70F", "6AEACFD8", "6F9F06F4", "EAFD9E2E",
      "32B655F7"]
v6 = v6[::-1]

def encrypt(a1, a2):
    v3 = 0
    v5 = a1[0]
    v6 = a1[1]
    for i in range(32):
        v3 += 1131796
        v5 += (a2[1] + (v6 >> 5)) ^ (v3 + v6) ^ (a2[0] + 16 * v6)
        v6 += (a2[3] + (v5 >> 5)) ^ (v3 + v5) ^ (a2[2] + 16 * v5)
    a1[0] = v5
    a1[1] = v6
    return 4


def decrypt(a10, a11, a2):
    v3 = 0x114514 * 32
    v5 = b2l(a10)
    v6 = b2l(a11)

    for i in range(32):
        v6 -= ((b2l(a2[2]) + (v5 >> 5)) ^ (v3 + v5) ^ (b2l(a2[3]) + 16 * v5)) & 0xffff
        v5 -= ((b2l(a2[1]) + (v6 >> 5)) ^ (v3 + v6) ^ (b2l(a2[0]) + 16 * v6)) & 0xffff
        v3 -= 0x114514
    print(l2b(v5), l2b(v6))
    a1 = l2b((v5 << 16) + v6)
    return a1


# def process_str(Str, v5):
#     v7 = bytearray(Str, 'utf-8')
#     for j in range(5):
#         sub_1400113E3(v7[j*8:(j+1)*8], v5)
#     return v7

# Convert the keys and ciphertexts to bytes
keys = [bytes.fromhex(item) for item in v5]
ciphertexts = [bytes.fromhex(item) for item in v6]

# Decrypt each block with each key
plaintexts = []
for i, j in zip(ciphertexts[::2], ciphertexts[1::2]):
    print(i, j)
    plaintexts.append(decrypt(i, j, keys))

print(plaintexts)

# for i in range(5):
#     hex_string = hex(flag[i])
#     char_string = bytearray.fromhex(hex_string[2:]).decode()
#     print(char_string, end='')
