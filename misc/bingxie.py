from Crypto.Cipher import AES
import base64

def decrypt_bingxie(enc_data, key):
    # Base64 decode the encrypted data
    enc = base64.b64decode(enc_data)

    # Create a new AES cipher object with the key and ECB mode
    aes_iv = AES.new(key, AES.MODE_ECB)

    # The IV is the first 16 bytes of the encrypted data
    iv = enc[:16]

    # Decrypt the IV
    decrypted_iv = aes_iv.decrypt(iv)

    # Initialize the decrypted data with the decrypted IV
    decrypted_data = decrypted_iv

    # Decrypt the rest of the data in 16-byte blocks
    for i in range(1, len(enc) // 16):
        # Create a new AES cipher object with the key, CBC mode, and the current IV
        aes = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt the current block
        decrypted_block = aes.decrypt(enc[i*16 : 16*(i+1)])

        # Append the decrypted block to the decrypted data
        decrypted_data += decrypted_block

        # Update the IV for the next block
        iv = enc[i*16 : 16*(i+1)]

    return decrypted_data

# Read the encrypted data from the 'enc' file
dir = 'F:\\BaiduNetdiskDownload\\数据安全省级决赛培训\\0919\\题目0919\\流量分析实操0919\\流量分析实操题\\流量分析实操题\\02、流量分析2\\'
with open(dir + 'answer_shell.txt', 'rb') as f:
    enc_data = f.read()

# The key for decryption
# key = '96468786d521366c'
key = '062292517173bf6d'
key = key.encode()

# Decrypt the data
decrypted_data = decrypt_bingxie(enc_data, key)

# Write the decrypted data to the 'data' file
with open('data', 'ab') as f:
    f.write(decrypted_data)
