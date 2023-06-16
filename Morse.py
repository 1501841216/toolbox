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

def decrypt(morse_code,_):
    inv_morse_code = {v: k for k, v in dict.items()}
    morse_code += ' '

    message = ''
    current_symbol = ''
    for char in morse_code:
        if char != _:
            current_symbol += char
        else:
            if current_symbol in inv_morse_code:
                message += inv_morse_code[current_symbol]
            else:

                if not found:
                    message += current_symbol  # Include unknown symbols as they are

            current_symbol = ''

    return message
