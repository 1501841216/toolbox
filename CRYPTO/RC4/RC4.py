# import base64
import myBASE
from Crypto.Util.number import *


def hex_to_str(hex_str):
    bytes_obj = bytes.fromhex(hex_str)
    return bytes_obj


def rc4_setup(key):
    """RC4初始化"""
    if isinstance(key, str):
        key = key.encode()

    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def rc4_crypt(data, key):
    """RC4加解密"""
    if isinstance(data, str):
        data = data.encode()

    S = rc4_setup(key)
    i, j = 0, 0
    res = []
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        res.append(byte ^ S[(S[i] + S[j]) % 256])

    return bytes(res)


def rc4_encrypt(data, key):
    """RC4加密"""
    return rc4_crypt(data, key)


def rc4_decrypt(data, key):
    """RC4解密"""
    return rc4_crypt(data, key)


def rc4_hex(key_hex, data_hex):
    """RC4加解密（16进制）"""
    key = bytes.fromhex(key_hex)
    data = bytes.fromhex(data_hex)
    res = rc4_crypt(data, key)
    return res.hex()


def rc4_encrypt_base64(data, key):
    """RC4加密并转换为base64格式"""
    encrypted_data = rc4_encrypt(data, key)
    # return base64.b64encode(encrypted_data).decode()
    return myBASE.base64encode(encrypted_data)


def rc4_decrypt_base64(data, key):
    """base64格式解码后RC4解密"""
    # encrypted_data = base64.b64decode(data)
    encrypted_data = myBASE.base64decode(data)
    return rc4_decrypt(encrypted_data, key).decode()


if __name__ == '__main__':
    plaintext = b'Thisismessage'
    key = b'BaseCTF'
    ciphertext_hex = "0ebb0c573dd548f3d2b2525f02895cd5275b6f6e5776538982ea41246dae8517"
    c = hex_to_str(ciphertext_hex)
    print(c)

    # RC4加密
    # ciphertext = rc4_encrypt(plaintext, key)
    # print("RC4加密", ciphertext)

    #RC4解密
    decrypted_text = rc4_decrypt(c, key)
    print("RC4解密", decrypted_text)

    # 16进制数据的RC4加解密
    # ciphertext_hex = rc4_hex(key.hex(), plaintext.hex())
    # print("16进制数据的RC4加密:", ciphertext_hex)

    # decrypted_text_hex = rc4_hex(key.hex(), ciphertext_hex)
    # print("16进制数据的RC4解密:", hex_to_str(decrypted_text_hex))
    #
    # # base64数据的RC4加解密
    # ciphertext_base64 = rc4_encrypt_base64(plaintext, key)
    # print("base64数据的RC4加密:", ciphertext_base64)
    #
    # decrypted_text_base64 = rc4_decrypt_base64(ciphertext_base64, key)
    # print("base64数据的RC4解密:", decrypted_text_base64)

