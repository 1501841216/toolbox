#3<<2可以这么算，bin(3)=0b11向左移动2位变成1100，0b1100=12(十进制)
def lfsr(R,mask):
    output = (R << 1) & 0xffffff    #将R向左移动1位，bin(0xffffff)='0b111111111111111111111111'=0xffffff的二进制补码
    i=(R&mask)&0xffffff             #按位与运算符&：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
    lastbit=0
    while i!=0:
        lastbit^=(i&1)    #按位异或运算符：当两对应的二进位相异时，结果为1
        i=i>>1
    output^=lastbit
    return (output,lastbit)

def inv_lfsr(output,lastbit, mask):
    output^=lastbit
    R = (output >> 1) & 0xffffff
    i = (R & mask) & 0xffffff
    while i!= 0:
        lastbit ^= (i & 1)
        i = i >> 1

    return (R, lastbit)

mask = 0b1010011000100011100

for i in range(12):
    tmp = 0
    for j in range(8):
        out =
        (R,out) = inv_lfsr(R,mask)
        tmp = (tmp >> 1)^out
