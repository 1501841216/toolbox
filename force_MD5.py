import hashlib


def hasmd5(arg):
    # 将数据转换成UTF-8格式
    se = hashlib.md5(arg.encode('utf-8'))
    # 将hash中的数据转换成只包含十六进制的数字
    result = se.hexdigest()
    return result

def verify_md5(input, md5_hash):
    # 计算输入的MD5哈希值
    input_hash = hashlib.md5(input.encode()).hexdigest()

    # 比较输入的哈希值与给定的哈希值
    return input_hash == md5_hash

dir = 'E:\\CTF\\CTFQD\\Crypto\\6c0c57fa88eb44f3b179a6e9798fc7b6'
#
# with open(dir, 'rb') as f:
#     data = f.read()
#     decoded = hasmd5(data)
#     print(decoded)
#     print(data)

account = 'admin'
password = '456'
md5_hash = '2b181c24cdb261bbff030042246b50fb'

# 尝试账号和密码的组合
for input in [account, password, account+password, password+account]:
    if verify_md5(input, md5_hash):
        print(f'The input "{input}" matches the given MD5 hash.')