from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import myBASE


def decrypt(encrypted_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text)
    # return unpad(decrypted_text, AES.block_size).decode()
    return decrypted_text

def decrypt_cbc(cipher_text, key, iv):
    c_bytes = myBASE.myb64decoder(cipher_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    c_bytes = pad(c_bytes, AES.block_size)
    decrypted_text = cipher.decrypt(c_bytes)


    return decrypted_text

def decrypt3(ciphertext, key, iv):
    # 将密钥和IV转换为字节
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')

    # Base64解码
    cipher_bytes = myBASE.myb64decoder(ciphertext)

    # 创建AES解密器
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

    # 解密
    decrypted_bytes = cipher.decrypt(cipher_bytes)

    # 去除零填充
    decrypted_bytes = decrypted_bytes.rstrip(b'\0')

    # 将解密结果转换为UTF-8字符串
    decrypted_text = decrypted_bytes.decode('utf-8')

    return decrypted_text

# key = '1234567890123456'
# iv = '1234567890123456'
# # cipher_text = 'iTMir0fEUm3GhQmNQk21WJ8z4AYmM6gvMZSDFwV1o8oZFHHi45AC+d3G3ja/V40sEzsKf4P8x7lyNhAdHUnKVoxtl/siqmgb/Y7qgO/34YW5S93rI652gjxWU13xbJKPwelvctrW7+F8vGm7AvP5SIxZbjfFzxAhuK8U+H+E/DTwSLy5ZXSjIo89mr6oyObgHjjCrjjHvSmBfnlV/DJyPQ=='
# # cipher_text = "lYjMuz6mqoL9oco0BLvxU4+s05vb4znN6e314fMtefxjKkyr4YSxVfHkvOPS0MZWNKbow8TNIEJ1u5vnZ1WBtVQXxcywtWsMT72glX6euyoDnCvqybLba9fbbjBaGtd++UaK7VsUuiU/tZXNGcqmcg==/"
# # cipher_text = 'bn8zqrVnVeedY85lFJEvCQG0DFZIqPGXagfK1bstdvspZP7VRxy9B8huWmoLam9PDF+61XHmQPUqvIW2XJs1kWzNR/RP88MhxJfhbzdl4gtcbW7s/5gH3I4yy5R0GtNU'
# cipher_text = '1BM2RTN5/+/PAZ042kMcyHkDLnkSXaDs/Luh2NvdyWd4M9Kb2gcZejUBGg64iHjN2QnnrnR+dBIXt3Puj06SCRMRvgkJtZyT4PZ4mRwURqQ='
# # c_bytes = base64.b64decode(cipher_text)
# decrypted_text = decrypt3(cipher_text, key, iv)
# print(decrypted_text)

# key = b"ThisIsASecretKey"
#
# encrypted_text="YC0ky5H1iE/1yvolTcavHPt8cla5DakNyXBlET1QXbnxQm3u7VVHlZjUc5XzVH6grI5HOoYPab0v\neu/TDaAPtg=="
#
# en=base64.b64decode(encrypted_text)
# print(en)
#
# decrypted_text = decrypt(en, key)
#
# print(base64.b64decode(decrypted_text))
# # b'flag{644b1f007a595ec4923b0a7de6fc809a}'

