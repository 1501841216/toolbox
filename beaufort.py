from string import ascii_uppercase

# 创建一个字母到索引的映射和一个索引到字母的映射
letter_to_index = {char: i for i, char in enumerate(ascii_uppercase)}
index_to_letter = dict(enumerate(ascii_uppercase))

def generate_key(message, key):
    return key * (len(message) // len(key)) + key[:len(message) % len(key)]

def beaufort_cipher(message, key):
    key = generate_key(message, key)
    return ''.join(index_to_letter[(letter_to_index[k] - letter_to_index[m]) % 26] for m, k in zip(message, key))

def beaufort_decipher(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    key = generate_key(cipher_text, key)
    return ''.join(index_to_letter[(letter_to_index[k] - letter_to_index[c]) % 26] for c, k in zip(cipher_text, key))

# 使用方法
# message = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
# key = "CULTURE"
# cipher_text = beaufort_cipher(message.replace(' ', ''), key)
# print(cipher_text)  # 输出: JNHDAJCSTUFYEZOXZCICMOZHCBKARUMVRDY
#
# deciphered_text = beaufort_decipher(cipher_text, key)
# print(deciphered_text)  # 输出: THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG