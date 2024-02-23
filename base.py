import base64
import string
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
    # print(data)

    return data

def myb32decoder(b32_str):
    # base32需要8字节对齐
    num_padding = 8 - (len(b32_str) % 8)
    if num_padding < 8:
        b32_str += "=" * num_padding

    data = base64.b32decode(b32_str)

    return data


# 将二进制数据写入文件
# with open("D:\\CTF\\crypto\\3.zip", "wb") as f:
#     f.write(myb64decoder(b64_str))

def decode_with_custom_base64(encoded_string, custom_alphabet):
    # Standard base64 alphabet
    standard_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'

    # Create a translation table
    translation_table = str.maketrans(custom_alphabet, standard_alphabet)

    # Translate the encoded string
    translated_string = encoded_string.translate(translation_table)

    # Decode the translated string
    decoded_string = base64.b64decode(translated_string)

    return decoded_string

# Usage
custom_alphabet = 'LAGRANGELAGRANGELAGRANGELAGRANGELAGRANGELAGRANGELAGRANGELAGRANGE'  # Should be 64 characters long
encoded_string = 'TVTTTVTXABYUXTXTXCARYYXAZCYYYUXV='
decoded_string = decode_with_custom_base64(encoded_string, custom_alphabet)
print(decoded_string)