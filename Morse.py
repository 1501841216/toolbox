dic = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
        }

def translate_characters(string,a,b):
    translation_table = str.maketrans(a+b, b+a)
    return string.translate(translation_table)

def Morse_encode(str):
    strr = ''
    for i in str:
        if i.upper() in dic:
            strr +=dic[i.upper()]
        else:
            # Include non-alphanumeric characters as they are
            strr += i
    return dic

def Morse_decode(str,_,a,b):
    #以_为划分，a，b其一充当点划
    inv_dic = {v: k for k,v in dic.items()}
    current_char = ''
    message = ''
    for char in str:
        #add _ at the end of the strinf, or the last word won't be recognized
        if char != _:
            current_char += char
        else:
            if char in inv_dic:
                message += inv_dic[current_char]
            else:
                inv_current_char = translate_characters(current_char,a,b)
                if inv_current_char in inv_dic:
                    message += inv_dic[inv_current_char]
                else:
                    print("wrong")
            current_char = ''

    return message