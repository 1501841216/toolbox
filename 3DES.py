from Crypto.Cipher import DES3
from Crypto.Util.number import long_to_bytes, bytes_to_long
from binascii import unhexlify
import rot

# 密文和密钥
ciphertext = "2qnss1sp48698op36o2q343sps9o7p0690s4r9s560or51qsnrqopsn8592439pno63695072qos1p3r"
key = "deluipuhgfnbcxsw"
ciphertext = rot.rot13(ciphertext)
# key = rot.rot13(key)
print(ciphertext)
cipher = DES3.new(key.encode(), DES3.MODE_ECB)
m = cipher.decrypt(ciphertext.encode())

print(m)
# # 密文和密钥
#
# # 创建一个3DES cipher对象，使用给定的密钥和ECB模式
# cipher = DES3.new(key.encode(), DES3.MODE_ECB)
#
# # 使用cipher对象解密密文
# plaintext_bytes = cipher.decrypt(ciphertext.encode())
#
# # 将解密后的字节串转换为字符串
# print(plaintext_bytes)