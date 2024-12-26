from Crypto.Util.number import long_to_bytes, bytes_to_long
import base64
import os, sys



str1 = "636A56355279427363446C4A49454A7154534230526D6843"
str2 = "56445A31614342354E326C4B4946467A5769426961453067"

print(long_to_bytes(int(str1, 16)))
print(long_to_bytes(int(str2, 16)))
# 转换为16进制

strr = long_to_bytes(int(str1, 16)) + b'\n' + long_to_bytes(int(str2, 16))
print(strr)

print(base64.b64decode(strr))

# 后根据键盘解密


# 打开文件
COOKED_FOLDER = 'E:\\CTF\\CTFQD\\Crypto'  # 文件夹的地址
file = '\\a7cefaacd1684bfdabd71b0e848c3b83.txt'
dirs = os.listdir(COOKED_FOLDER)
filepath = COOKED_FOLDER + file  # 文件所在地址
with open(filepath, 'r') as f:
    for line in f:
        print("new")
        print(long_to_bytes(int(line, 16)))