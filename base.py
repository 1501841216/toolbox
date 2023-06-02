import base64
c = "ZmxhZ3tiGNXlXjHfaDTzN2FfK3LycRTpc2L9"
#Custom base64 table
str_custom_base = "ABCDEFQRSTUVWXYPGHIJKLMNOZabcdefghijklmnopqrstuvwxyz0123456789+/"
#zh base64 table
str_zh_base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
flag = base64.b64decode(c.translate(str.maketrans(str_custom_base,str_zh_base)))
temp = str.maketrans(str_custom_base,str_zh_base)
print(temp)
print(c.translate(temp))
print(flag)