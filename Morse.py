import re

dic = {'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..', 'E': '.', 'F': '.._.',
       'G': '__.', 'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..',
       'M': '__', 'N': '_.', 'O': '___', 'P': '.__.', 'Q': '__._', 'R': '._.',
       'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
       'Y': '_.__', 'Z': '__..',
       '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....',
       '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '_____',
       ' ': ' '}
def Morse_encode(str):
    strr = ''
    for i in str:
        if i.upper() in dic:
            strr += dic[i] + ' '
        else:
            strr += i
    return strr

def decrypt(morse_code,spliter, dot, line):
    inv_dic = {v: k for k, v in dic.items()}
    message = ''
    morse_list = morse_code.split(spliter)
    for elemt in morse_list:
        data = elemt.replace(line, '_')
        print(data)
        assert data in inv_dic
        message += inv_dic[data]

    return message

