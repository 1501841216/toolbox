import base64
# c = "ZmxhZ3tiGNXlXjHfaDTzN2FfK3LycRTpc2L9"
# #Custom base64 table
# str_custom_base = "ABCDEFQRSTUVWXYPGHIJKLMNOZabcdefghijklmnopqrstuvwxyz0123456789+/"
# #zh base64 table
# str_zh_base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# flag = base64.b64decode(c.translate(str.maketrans(str_custom_base,str_zh_base)))
# temp = str.maketrans(str_custom_base, str_zh_base)
# print(temp)
# print(c.translate(temp))
# print(flag)


# 带有不足4个字符的Base64编码字符串
# b64_str = "RmbTNeOdQSwECPwAKAAEIAABibQpJ9LUJHx4AAAASAAAACAAkAAAAAAAAACAAAAAAAAAAZmxhZy50eHQKACAAAAAAAAEAGACvFQIQyvLRAVyuqgXK8tEBXK6qBcry0QFQSwUGAAAAAAEAAQBaAAAARAAAAAAA"
# b64_str = "TlRMTVNTUAACAAAACAAIADgAAAAVgonicGVadiRM4ywAAAAAAAAAAHgAeABAAAAABgOAJQAAAA9RAEoAWQBDAAIACABRAEoAWQBDAAEAEABIAFIAUwBFAFIAVgBFAFIABAAOAHEAagB5AGMALgBjAG4AAwAgAEgAUgBTAEUAUgBWAEUAUgAuAHEAagB5AGMALgBjAG4ABQAOAHEAagB5AGMALgBjAG4ABwAIAMJpv2bWFdoBAAAAAA=="

def myb64decoder(b64_str):
    # 计算需要添加的等号数
    num_padding = 4 - (len(b64_str) % 4)
    if num_padding < 4:
        b64_str += "=" * num_padding

    # 解码为二进制数据
    data = base64.b64decode(b64_str)
    print(data)

    return data

# 将二进制数据写入文件
# with open("D:\\CTF\\crypto\\3.zip", "wb") as f:
#     f.write(myb64decoder(b64_str))

