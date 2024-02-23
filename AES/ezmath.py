from Crypto.Util.number import *
from Crypto.Cipher import AES
import random,string
import AES_ecb
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq
from sympy.solvers.diophantine import diop_solve

#http://www.numbertheory.org/php/pell.html
enc=b"\xce\xf1\x94\x84\xe9m\x88\x04\xcb\x9ad\x9e\x08b\xbf\x8b\xd3\r\xe2\x81\x17g\x9c\xd7\x10\x19\x1a\xa6\xc3\x9d\xde\xe7\xe0h\xed/\x00\x95tz)1\\\t8:\xb1,U\xfe\xdec\xf2h\xab`\xe5'\x93\xf8\xde\xb2\x9a\x9a"

def pad(x):
    return x+b'\x00'*(16-len(x)%16)

def draw():
    y = np.linspace(-1000000, 1000000, 400)

    x = np.sqrt(1 + 114514*y**2)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color="red", linewidth=2)
    plt.plot(-x, y, color="green", linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of the equation x^2 - 114514*y^2 = 1')
    plt.legend()
    plt.grid(True)
    plt.show()

x,y = 3058389164815894335086675882217709431950420307140756009821362546111334285928768064662409120517323199,9037815138660369922198555785216162916412331641365948545459353586895717702576049626533527779108680
key = pad(long_to_bytes(y))[:16]
print(AES_ecb.decrypt(enc, key))