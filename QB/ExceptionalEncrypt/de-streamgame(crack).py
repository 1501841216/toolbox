def lfsr(R, mask):
    output = (R << 1) & 0xffffff    #将R向左移动1位，bin(0xffffff)='0b111111111111111111111111'=0xffffff的二进制补码
    i= (R&mask) & 0xffffff             #按位与运算符&：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
    lastbit = 0
    while i != 0:
        lastbit ^= (i&1)    #按位异或运算符：当两对应的二进位相异时，结果为1
        i=i>>1
    output^=lastbit
    return (output,lastbit)

mask = 0b0001010011000100011100
home = 'E:\\CTF\\CTFQD\\Crypto\\e05281b9394c4032b443f9793b76be2a\\'
f = open(home + "key",'rb')
data = f.read()
key = []
for i in data:
    zfnum = "%08d" % int(bin(i).replace('0b', ''))
    key.append(zfnum)
print(key)

for k in range(2**19):
    R = k
    tip = 1
    for i in range(12):
        tmp = 0
        for j in range(8):
            (R,out) = lfsr(R,mask)
            tmp = (tmp<<1)^ out
        if tmp != int(key[i],2):
            tip = 0
            break
    if tip == 1:
        print(k)
        break