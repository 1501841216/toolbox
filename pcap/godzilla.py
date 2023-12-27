from Crypto.Cipher import AES
import binascii
import zlib

# 密钥，与 JSP 代码中的密钥相同
key = b'748007e861908c03'

# 要解密的加密数据（十六进制形式）
# encrypted_hex_data = "b5c1fadbb7e28da08572486d8e6933a84c5144463f178b352c5bda71cff4e8ffe919f0f115a528ebfc4a79b03aea0e31cb22d460ada998c7657d4d0f1be71ffa"
encrypted_hex_data = "b5c1fadbb7e28da08572486d8e6933a84c5144463f178b352c5bda71cff4e8ffe919f0f115a528ebfc4a79b03aea0e31cb22d460ada998c7657d4d0f1be71ffa"

from Crypto.Util.Padding import pad, unpad

def decode(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data, AES.block_size)  # Add padding
    decrypted_data = cipher.decrypt(padded_data)
    return unpad(decrypted_data, AES.block_size)  # Remove padding

# def decode(data, key):
#     cipher = AES.new(key, AES.MODE_ECB)
#     decrypted_data = cipher.decrypt(data)
#     return decrypted_data

def ungzip(in_str):
    s = zlib.decompress(in_str, 16 + zlib.MAX_WBITS).decode()
    print("Decoded and Unzipped:\n", s)

# 将十六进制数据转换为字节序列
encrypted_bytes = bytes.fromhex(encrypted_hex_data)
# print(encrypted_bytes)
encrypted_bytes = pad(encrypted_bytes, AES.block_size)
# print(encrypted_bytes)

# 解密数据并解压缩
decrypted_data = decode(encrypted_bytes, key)
print(decrypted_data)
ungzip(decrypted_data)
