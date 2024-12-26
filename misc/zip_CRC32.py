import zipfile  # 导入zipfile模块，用于处理zip文件

import string  # 导入string模块，用于生成字母和数字

import binascii  # 导入binascii模块，用于进行CRC32校验

import os  # 导入os模块，用于文件操作

filepath = 'F:/CTF/CTFQD/games/2024wdcup/2024wdzq/misc/01d8dd2bbb20c19f31776d1829a99cc5/_veryeasy.png.extracted/'  # 设置文件路径

os.chdir(filepath)  # 切换当前工作目录为指定路径


def CrackCrc(crc):
    # 定义一个函数用于破解CRC32校验值

    for i in dic:

        for j in dic:

            for k in dic:

                for h in dic:

                    s = i + j + k + h  # 生成四个字符的组合

                    if crc == (binascii.crc32(s.encode())):  # 判断CRC32校验值是否匹配

                        f.write(s)  # 将匹配的字符串写入文件

                        return


def CrackZip():
    # 定义一个函数用于破解zip文件

    for i in range(0, 68):
        file = filepath + '18315A' + str(i) + '.zip'  # 构造zip文件名

        crc = zipfile.ZipFile(file, 'r').getinfo('data.txt').CRC  # 获取zip文件中data.txt的CRC32校验值

        CrackCrc(crc)  # 调用破解CRC32校验值的函数

        print('\r' + "loading：{:%}".format(float((i + 1) / 68)), end='')  # 打印加载进度


dic = string.ascii_letters + string.digits + '+/='  # 定义字符集，包括大小写字母、数字和'+/='符号

f = open('out.txt', 'w')  # 打开一个文件用于写入破解结果

print("\nCRC32begin")  # 打印开始破解提示

CrackZip()  # 调用破解zip文件的函数

print("CRC32finished")  # 打印破解完成提示

f.close()  # 关闭文件