# 1. string 可以encode变成字节流，也可以decode回来 “msg.encode().decode()”
# 2. 这里用正则作替换，与GFSJO827-sherlock作对比

import re
from Crypto.Util.number import long_to_bytes, bytes_to_long
import base64
import Morse

home  = "D:\\CTF\\crypto\\"

s = ""

with open(home + "cca1ce4b15ba4ac7950f6d03f8fa6ad1",'rb') as f:
        line = f.read().decode().replace(' ','')
        print(line)
        data = re.sub(r'ZERO', '0', re.sub(r'ONE', '1', line)).strip()
        print(data)
        morse_code = base64.b64decode(long_to_bytes(int(data, 2))).decode()
        print(morse_code)
        print(Morse.decrypt(morse_code,' ', '.', '-'))
        f.close()


