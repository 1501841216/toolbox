from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def decrypt(encrypted_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(encrypted_text)
    # return unpad(decrypted_text, AES.block_size).decode()
    return decrypted_text


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