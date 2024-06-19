import binascii
from Crypto.Util.number import long_to_bytes
# x_xor_md5

def read_file_as_hex(filename):
    with open(filename, 'rb') as file:
        content = file.read()
    return binascii.hexlify(content)

def xor_hex(hex_content, key):
    # 将十六进制字符串转换为二进制数据
    content = binascii.unhexlify(hex_content)
    key = binascii.unhexlify(key)

    # 确保key的长度与content的长度相同
    if len(key) < len(content):
        key = (key * (len(content) // len(key) + 1))[:len(content)]

    # 进行异或操作
    xor_result = bytearray([b ^ k for b, k in zip(content, key)])

    # 将结果转换回十六进制字符串
    return binascii.hexlify(xor_result).decode()
    # return xor_result


# 使用函数
dir = "E:\\CTF\\CTFQD\\Crypto\\6c0c57fa88eb44f3b179a6e9798fc7b6\\6c0c57fa88eb44f3b179a6e9798fc7b6"
hex_content = read_file_as_hex(dir)
key = hex_content[160:192]
key = xor_hex(key, '20')
print(key)

for i in range(0, len(hex_content), 32):
    c = hex_content[i:i+32]
    m = xor_hex(c, key)
    m = binascii.unhexlify(m)
    s = ''
    for i in m:
        if i >= 42 and i <= 126:
            s += chr(i)
        else:
            s += str(i)
    print(s)