from random import randint

c1 = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!"
c2 = "_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"
def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def encrypt(m):
    c = ''
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha():
            ech = ch
        else:
            chi = to_identity_map(ch)
            ech = from_identity_map(chi + i)
        c += ech
    return c

def decrypt(c):
    m = ''
    for i in range(len(c)):
        ch = c[i]
        if not ch.isalpha():
            mch = ch
        else:
            mch = chr((ord(ch)-0x41 - i) % 26 + 0x41)
        m += mch
    return m

m1 = decrypt(c1)
print(m1)
m2 = decrypt(c2)
print(m2)
c3 = c1 + c2
m3 = decrypt(c3)
print(m3)
