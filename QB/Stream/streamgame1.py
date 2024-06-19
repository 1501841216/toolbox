#3<<2可以这么算，bin(3)=0b11向左移动2位变成1100，0b1100=12(十进制)
from Crypto.Util.number import long_to_bytes, bytes_to_long
def lfsr(R, mask):                  # 打印出R的四位
    output = (R << 1) & 0xffffff
    print('output:', bin(output)[2:].zfill(24))# r左移一位，并保持24位
    i = (R & mask) & 0xffffff   # 取R的第二位
    print('i     :', bin(i)[2:].zfill(24))              # i为r和mask的混合
    lastbit = 0                       # 每次开始lastbit置零
    while i != 0:                     # 判断i中1的个数，若为奇数，lastbit为1，若为偶数，lastbit为0
        lastbit ^= (i & 1)
        # print('while i != 0, i&1 = ',i&1)
        i = i >> 1
        # print('while i !=0 ,i = ',bin(i)[2:].zfill(24))
        # print('while i !=0, lastbit = ', lastbit)
    output^=lastbit                 # 记录R&mask中1的奇偶性

    return (output,lastbit)         # 输出r左移一位加记录值，以及i的奇偶性



mask = 0b1010011000100011100
home = 'E:\\CTF\\CTFQD\\Crypto\\e05281b9394c4032b443f9793b76be2a\\'


R = 0xffffff
for i in range(12):
    tmp = 0
    print('12R   :',bin(R)[2:].zfill(24))
    for j in range(8):
        (R,out) = lfsr(R,mask)
        print('R     :',bin(R)[2:].zfill(24))
        print('lastbit:',out)
        tmp = (tmp<<1)^ out
    print(bin(tmp))