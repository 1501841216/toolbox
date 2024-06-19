import binascii
import base64
import re

def decrypt(str):
    xor_key = 45
    m = bytearray()
    for i in range(len(str)):
        m.append(str[i] ^ xor_key)
        xor_key = ((xor_key ^ 99) ^ (i%254))
    return m

def decrypt_file(file_path, pattern, offset, length):
    with open(file_path, 'rb') as file:
        data = file.read()

    start_index = data.find(pattern)
    if start_index == -1:
        print('Pattern not found in the file.')
        return

    start_index += offset-1
    print(hex(start_index))
    data_to_decrypt = data[start_index:start_index+length]
    print(data_to_decrypt)
    decrypted_data = decrypt(data_to_decrypt)
    print(len(decrypted_data))
    return decrypted_data

file_dir = 'E:\\CTF\\CTFQD\\games\\2024cyber_appocalypse\\forensics_game_invitation\\00000000\\word\\media\\image1.jpg'
pattern = b'sWcDWp36x5oIe2hJGnRy1iC92AcdQgO8RLioVZWlhCKJXHRSqO450AiqLZyLFeXYilCtorg0p3RdaoPa'
offset = 81
length = 13082
key = 'vF8rdgMHKBrvCoCp0ulm'

decrypted_data = decrypt_file(file_dir, pattern, offset, length)
# if decrypted_data is not None:
#     print('Decrypted data:', decrypted_data)
r = (re.search(b'var r="(.*?)";', decrypted_data)).group(1)
print(r)

def af5Q(r):
    a = r
    if a == 43 or a == 45:
        return 62
    if a == 47 or a == 95:
        return 63
    if a < 48:
        return -1
    if a < 48 + 10:
        return a - 48 + 26 + 26
    if a < 65 + 26:
        return a - 65
    if a < 97 + 26:
        return a - 97 + 26

def JrvS(r):
    # r = bytes(r, 'utf-8')  # 将输入字符串转换为字节流
    n = []
    u = len(r)
    g = 2 if r[u-2] == ord('=') else 1 if r[u-1] == ord('=') else 0
    i = u - 4 if g > 0 else u
    z = 0

    for t in range(0, i, 4):
        h = af5Q(r[t]) << 18 | af5Q(r[t+1]) << 12 | af5Q(r[t+2]) << 6 | af5Q(r[t+3])
        n.append((h & 16711680) >> 16)
        n.append((h & 65280) >> 8)
        n.append(h & 255)

    if g == 2:
        h = af5Q(r[i]) << 2 | af5Q(r[i+1]) >> 4
        n.append(h & 255)
    elif g == 1:
        h = af5Q(r[i]) << 10 | af5Q(r[i+1]) << 4 | af5Q(r[i+2]) >> 2
        n.append(h >> 8 & 255)
        n.append(h & 255)

    return bytes(n)

print(JrvS(r))

def xR68(r, a):
    t = list(range(256))
    l = 0
    u = ""
    for g in range(256):
        l = (l + t[g] + ord(r[g % len(r)])) % 256
        t[g], t[l] = t[l], t[g]
    g = l = 0
    for n in range(len(a)):
        g = (g + 1) % 256
        l = (l + t[g]) % 256
        t[g], t[l] = t[l], t[g]
        u += chr(a[n] ^ t[(t[g] + t[l]) % 256])
    return u

print(xR68(key, JrvS(r)))


