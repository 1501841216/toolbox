from Crypto.Cipher import DES
#
# flag = b"flag{**********}"
# key = b'*********'
#
#
# cipher = DES.new(key.encode(), DES.MODE_ECB)
# msg = cipher.decrypt(flag)
# print(msg.hex)
#
# assert str(int(key)) == key.decode()
# assert key[:3] == b'952'

# The encrypted message
msg = 0x5defdf5206488c386d1b996b045c85db

# Convert the encrypted message from hexadecimal to bytes
msg_bytes = msg.to_bytes((msg.bit_length() + 7) // 8, 'big')

# The known part of the key
known_key = '952'

# Try all possible combinations for the remaining part of the key
for i in range(10000, 100000):  # 5 digits
    # Construct the key
    key = (known_key + str(i)).encode()

    # Create a new DES cipher object
    cipher = DES.new(key, DES.MODE_ECB)

    # Decrypt the message
    flag = cipher.decrypt(msg_bytes)

    # If the decrypted message starts with 'flag', we found the correct key
    if flag.startswith(b'flag'):
        print('Found the key:', key)
        print('Decrypted flag:', flag)
        break


