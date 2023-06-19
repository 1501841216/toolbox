from Crypto.Util.number import long_to_bytes, bytes_to_long
import base64


str1 = "636A56355279427363446C4A49454A7154534230526D6843"
str2 = "56445A31614342354E326C4B4946467A5769426961453067"

print(long_to_bytes(int(str1, 16)))
print(long_to_bytes(int(str2, 16)))

strr = long_to_bytes(int(str1, 16)) + b'\n' + long_to_bytes(int(str2, 16))
print(strr)

print(base64.b64decode(strr))

# 后根据键盘解密

