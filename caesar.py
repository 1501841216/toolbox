def caesar_cipher(plaintext, shift):
    """
    加密函数，将明文移位加密成密文
    :param plaintext: 待加密的明文
    :param shift: 移位数，可正可负
    :return: 加密后的密文
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += shift_char
        else:
            ciphertext += char
    return ciphertext

def caesar_decode(ciphertext, shift):
    """
    解密函数，将密文还原成明文
    :param ciphertext: 待解密的密文
    :param shift: 移位数，与加密时的 shift 相同
    :return: 解密后的明文
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += shift_char
        else:
            plaintext += char
    return plaintext
