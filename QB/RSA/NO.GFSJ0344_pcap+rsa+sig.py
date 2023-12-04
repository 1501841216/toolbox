from Crypto.PublicKey import RSA
import  Crypto.Signature.pkcs1_15 as pkcs1_15
import gmpy2
# import base
import base64
import myRSA
import re

# Alice's public encryption parameters
n13 = 1696206139052948924304948333474767
e = 65537

# Bob's
n37 = 3104649130901425335933838103517383

# Yes! We can factorize the n
p13 = 38456719616722997
q13 = 44106885765559411

p37 = 49662237675630289
q37 = 62515288803124247

# that means we can find the decryption exponent d
phi1 = (p13 - 1) * (q13 - 1)
phi2 = (p37 - 1) * (q37 - 1)
d13 = gmpy2.invert(e, phi1)
d37 = gmpy2.invert(e, phi2)

# now construct the RSA with all the parameters
rsa13 = RSA.construct((n13, e, int(d13)))
rsa37 = RSA.construct((n37, e, int(d37)))

# and decrypt the messages from a pcap file!
# from pcapfile import savefile
home = 'D:\\CTF\\crypto\\f9ba6369b331427eb4f401988f5e6b83\\'
# cf = savefile.load_savefile(open(home + "test.pcap"))
#
# output = {}
#
# for p in cf.packets:
#     pack = str(p.packet)[136:].decode('hex').decode('base64')
#     if 'DATA' in pack:
#         seq = int(pack.split(';')[0].split(' ')[2])
#         data = pack[16:].split(';')[0][:-1]
#         sig = int(pack.split(';')[2].split(' = ')[1], 16)
#         c = int(data, 16)
#         decrypted = rsa2.decrypt(c)
#         sigcheck = rsa1.sign(decrypted, '')[0]
#         val = str(hex(decrypted)).strip('0x').rstrip('L').zfill(2).decode('hex')
#         if sig == sigcheck:
#             output[seq] = val
# print(''.join(output.values()))

f = open(home + 'b64_str')
data = f.read()
dic = {}
for i in data.split('\n'):
    # deb64 = base.myb64decoder(i).decode()
    deb64 = base64.b64decode(i).decode()
    print(deb64)
    seq = int(re.findall(r"SEQ = (.*?);",deb64)[0])
    print(seq)
    c1 = int(re.findall(r"DATA = (.*?)L;",deb64)[0],16)
    c2 = int(re.findall(r"SIG = (.*?)L;",deb64)[0],16)
    # decrypted = rsa37._decrypt(c1)
    # decrypted = myRSA.ndc_4_m(n37, int(d37), c1)
    decrypted = myRSA.verify(rsa13, rsa37, c1, c2)
    # 解码的信息和验证的信息一致才行
    if decrypted[0] == decrypted[1]:
        dic[seq] = decrypted[0]
    # dic[int(seq)] = decrypted
    # print(decrypted[0])
    # print(decrypted[1])
#     # pkcs1_15.new(rsa13).verify(c1,c2)
#     # print(rsa13.sign(decrypted, ''))
#
sorted_d = dict(sorted(dic.items(), key=lambda x: x[0]))
print(sorted_d)
flag = ''
for i in sorted_d.values():
    flag += i.decode()
print(flag)