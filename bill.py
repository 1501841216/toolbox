 # -*- coding:utf-8 -*-
import re


def bill(file, c, key):
    # file="wheelcipher.txt"
    # c = "NFQKSEVOQOFNP"
    # key = "2,3,7,5,13,12,9,1,8,10,4,11,6"

    text = ""
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    # print (text) 查看是否读取完整
    code = []
    # 将"<...<"中的字符提取出来放在code里
    code = re.findall(r"<(.*)<", text)
    for i in range(len(code)):
        code[i] = code[i].strip()
    print(code)
    key = key.split(",")
    # 把这些数字都弄到一个里面去
    # print(c)
    a = 0
    print("解密后的：")
    for i in key:
        index = code[int(i)-1].index(c[a])
        a = a+1
        code[int(i)-1] = code[int(i)-1][index:]+code[int(i)-1][:index]
        print(code[int(i)-1])

    # 完成了变形了
    print(code)
    print("下面是每一列的")
    for i in range(len(code[0])):
        temp = ""
        print("第{}列的是:".format(i), end="")
        for j in key:
            temp += code[int(j)-1][i]
        print(temp.lower())