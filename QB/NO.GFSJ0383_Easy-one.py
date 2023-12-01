import binascii
# The known-plaintext attack (KPA) is an attack model for cryptanalysis where the attacker has samples of both the plaintext (called a crib), and its encrypted version (ciphertext). These can be used to reveal further secret information such as secret keys and code books. The term "crib" originated at Bletchley Park, the British World War II decryption operation.



def encrypt(home,message):
    k = "VeryLongKeyYouWillNeverGuess"
    t = 0
    i = 0
    with open(home + 'testc', 'wb') as f:
        for p in message:
            print(p)
            print(chr(p))
            # p = int.from_bytes(p, byteorder='big')
            c=chr((p + (ord(k[i%len(k)])^t) + i*i) & 0xff)
            t = p
            i += 1
            f.write(c.encode())
            print(c)

def decrypt(home, cipher):
    k = "VeryLongKeyYouWillNeverGuess"
    m = ''
    t = '\0'
    i = 0
    with open(home + 'testm', 'wb') as f:
        for c in cipher:
            # print(p)
            # p = int.from_bytes(p, byteorder='big')
            # print(m)
            m = chr((c-(ord(k[i%len(k)])^ord(t))-i*i)%128)
            f.write(m.encode())
            t = m
            i += 1
            print(m)

def crackK(message,cipher):
    t = 0
    i = 0
    k = ''
    if len(message) != len(cipher):
        print("length error")
        return
    for j in range(len(message)):
        k += chr(((cipher[j]-message[j]-i*i)^t)&0xff)
        t = message[j]
        i += 1
    print(k)


home = 'E:\\CTF\\CTFQD\\Crypto\\491476abacd445d19e7dd9dfa474f9d1\\'
f = open(home + 'msg001', 'rb')
message = f.read()
# print(data)
# # message = []
# # for i in range(0, len(data), 1):
# #     message.append(data[i:i+1])
print(message)

f = open(home + 'msg001.enc', 'rb')
cipher = f.read()
print(cipher)

# encrypt(home, message)
# decrypt(home, cipher)
crackK(message,cipher)

