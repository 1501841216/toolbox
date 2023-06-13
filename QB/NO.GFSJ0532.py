#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
# Version: Python 2.7

import base64


def encode1(ans):
    s = ''
    for i in ans:
        x = i ^ 36
        x = x + 25
        s += chr(x)

    return s


def inv_encode1(ans):
    s = ''
    for i in ans:
        x = ord(i) - 25
        x = x ^ 36
        s += chr(x)

    return s


def encode2(ans):
    s = ''
    for i in ans:
        x = ord(i) + 36
        x = x ^ 36
        s += chr(x)

    return s


def inv_encode2(ans):
    s = ''
    for i in ans:
        x = i ^ 36
        x = x - 36
        s += chr(x)

    return s


def encode3(ans):
    return base64.b32encode(ans)


def inv_encode3(ans):
    return base64.b32decode(ans)



final = 'UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==='
# if encode3(encode2(encode1(flag))) == final:
#     print
#     'correct'
# else:
#     print
#     'wrong'

d1 = inv_encode3(final)
print(d1)
d2 = inv_encode2(d1)
print(d2)
d3 = inv_encode1(d2)
print(d3)