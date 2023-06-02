def fence_cipher_encrypt(plain_text, rails):
    # 创建一个二维列表来表示栅栏
    fence = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
    direction = -1  # 控制栅栏的上下方向
    row, col = 0, 0  # 当前位置的行和列

    # 在栅栏上填充明文字符
    for char in plain_text:
        if row == 0 or row == rails - 1:
            direction = -direction  # 当到达栅栏的边界时，改变方向

        fence[row][col] = char  # 将字符放入栅栏的当前位置
        col += 1  # 移动到下一列
        row += direction  # 根据方向移动到下一行

    cipher_text = ''
    # 按顺序从栅栏中提取密文字符
    for i in range(rails):
        for j in range(len(plain_text)):
            if fence[i][j] != '\n':
                cipher_text += fence[i][j]

    return cipher_text


def fence_cipher_decrypt(cipher_text, rails):
    # 创建一个二维列表来表示栅栏，长为len(cipher_text)，宽为rail
    fence = [['\n' for _ in range(len(cipher_text))] for _ in range(rails)]
    print(fence)
    direction = -1  # 控制栅栏的上下方向
    row, col = 0, 0  # 当前位置的行和列

    # 在栅栏上标记用于填充的位置
    for _ in range(len(cipher_text)):
        if row == 0 or row == rails - 1:
            direction = -direction  # 当到达栅栏的边界时，改变方向

        fence[row][col] = '*'  # 标记填充位置
        col += 1  # 移动到下一列
        row += direction  # 根据方向移动到下一行

    index = 0
    # 将密文字符填入栅栏的填充位置
    for i in range(rails):
        for j in range(len(cipher_text)):
            if fence[i][j] == '*' and index < len(cipher_text):
                fence[i][j] = cipher_text[index]
                index += 1

    plain_text = ''
    row, col = 0, 0
    # 从栅栏中提取明文字符
    for _ in range(len(cipher_text)):
        if row == 0 or row == rails - 1:
            direction = -direction  # 当到达栅栏的边界时，改变方向

        if fence[row][col] != '*':
            plain_text += fence[row][col]  # 提取字符
        col += 1  # 移动到下一列
        row += direction  # 根据方向移动到下一行

    return plain_text


