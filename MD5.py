import hashlib


def hasmd5(arg):
    # 将数据转换成UTF-8格式
    se = hashlib.md5(arg.encode('utf-8'))
    # 将hash中的数据转换成只包含十六进制的数字
    result = se.hexdigest()
    return result