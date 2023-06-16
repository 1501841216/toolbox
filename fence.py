def encrypt_fence(plain_text, rails):
    fence = [[''] * len(plain_text) for _ in range(rails)]  # 创建栅栏矩阵
    rail = 0  # 当前栅栏的行数
    direction = 1  # 栅栏遍历方向（向上或向下）

    for char in plain_text:
        fence[rail][fence[rail].index('')] = char  # 将字符填入栅栏矩阵
        rail += direction  # 移动到下一行

        if rail == rails - 1 or rail == 0:
            direction *= -1  # 到达栅栏的边界时，改变遍历方向

    encrypted_text = ''
    for row in fence:
        encrypted_text += ''.join(row)  # 将栅栏矩阵中的字符连接成加密文本

    return encrypted_text


def decrypt_fence(cipher_text, rails):
    fence = [[''] * len(cipher_text) for _ in range(rails)]  # 创建栅栏矩阵
    rail = 0  # 当前栅栏的行数
    direction = 1  # 栅栏遍历方向（向上或向下）

    for _ in range(len(cipher_text)):
        fence[rail][fence[rail].index('')] = '*'  # 在栅栏矩阵中用占位符标记位置
        rail += direction  # 移动到下一行

        if rail == rails - 1 or rail == 0:
            direction *= -1  # 到达栅栏的边界时，改变遍历方向

    index = 0
    for row in fence:
        for i in range(len(row)):
            if row[i] == '*':
                row[i] = cipher_text[index]  # 将密文字符填入栅栏矩阵
                index += 1

    rail = 0  # 当前栅栏的行数
    direction = 1  # 栅栏遍历方向（向上或向下）
    decrypted_text = ''
    for _ in range(len(cipher_text)):
        decrypted_text += fence[rail][0]  # 从栅栏矩阵中取出字符
        fence[rail][0] = ''  # 将取出的字符置为空
        rail += direction  # 移动到下一行

        if rail == rails - 1 or rail == 0:
            direction *= -1  # 到达栅栏的边界时，改变遍历方向

    return decrypted_text
