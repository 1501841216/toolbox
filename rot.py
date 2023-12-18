def rot13(text):
    result = ""

    for char in text:
        ascii_val = ord(char)

        if ascii_val >= ord('a') and ascii_val <= ord('z'):
            result += chr((ascii_val - ord('a') + 13) % 26 + ord('a'))
        elif ascii_val >= ord('A') and ascii_val <= ord('Z'):
            result += chr((ascii_val - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char

    return result