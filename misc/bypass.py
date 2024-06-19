from sympy import true

blacklist = [';', '"', 'os', '_', '\\', '/', '`',
             ' ', '-', '!', '[', ']', '*', 'import',
             'eval', 'banner', 'echo', 'cat', '%',
             '&', '>', '<', '+', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', '0', 'b', 's',
             'lower', 'upper', 'system', '}', '{']

def try_to_bypass():
    ans = input('Break me, shake me!\n$ ').strip()
    print(ans + '()')

    # if any(char in ans for char in blacklist):
    #     print(f'Naughty naughty..\n')
    for char in ans:
        if char in blacklist:
            print(f'Naughty naughty.. The character "{char}" is in the blacklist.\n')
    else:
        try:
            eval(ans + '()')
            print('WHAT WAS THAT?!\n')
        except:
            print(f"I'm UNBREAKABLE!\n")

while true:
    try_to_bypass()
