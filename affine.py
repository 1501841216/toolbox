# 不仅适用于26个字母，还加上去其他符号
import gmpy2
import base
import re


def make_table():
    table = []
    for i in range(26):
        table += chr(i+65)
    for j in range(2,8):
        table += str(j)
    return table

def generalized_encrypt(a,b,msg,table):
    msg = msg.upper()
    c = ""
    for i in msg:
        if i == " ":
            c += " "
        else:
            c += table[((a*table.index(i)+b)%len(table))]
    return c

def generalized_decrypt(a,b,cipher,table):
    cipher = cipher.upper()
    msg = ""
    for i in cipher:
        if i == " ":
            msg += " "
        else:
            assert gmpy2.invert(a,len(table)) != 0
            msg += table[((table.index(i)-b)*gmpy2.invert(a,len(table)))%len(table)]
    return msg

def specialized_encrypt(a,b,msg):
    msg = msg.upper()
    c = ""
    for i in msg:
        if i == " ":
            c += " "
        else:
            c += chr(((a*(ord(i)-65)+b)%26)+65)
    return c

def specialized_decrypt(a,b,cipher):
    cipher = cipher.upper()
    msg = ""
    for i in cipher:
        if i == " ":
            msg += " "
        else:
            assert gmpy2.invert(a,26) != 0
            msg += chr((((ord(i)-65)-b)*gmpy2.invert(a,26))%26+65)
    return msg

# pad 为尝试破解的数的范围,a,b,m
def crack(enc, a_pad, b_pad, m_pad,table):
    for i in range(0,a_pad):
        for j in range(0,b_pad):
            for k in range(0,m_pad):
                try:
                    s = generalized_decrypt(i,j,enc,table)
                    flag = base.myb32decoder(s)
                    # if b'{'in flag and b'}' in flag:
                    #     print(flag)
                    if re.match(b'^\w+([-+.]\w+)*\{\w+([-.]\w+)*\}$', flag):
                        print(flag)
                except:
                    pass
                s = ''


tab = make_table()
print(tab)
msg = 'IJEVIU2DKRDHWUZSKZ4VSMTUN5RDEWTNPU'
cipher = 'MZYVMIWLGBL7CIJOGJQVOA3IN5BLYC3NHI'
#
# print(generalized_encrypt(13,4,msg,table))
# print(generalized_decrypt(13,4,cipher,table))

crack(cipher,33,33,33,tab)


