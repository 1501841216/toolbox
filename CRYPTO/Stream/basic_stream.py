# 加密公式：c = m ^ key 已知： c = "cidb~c4wvqZvq`<$$x" key = 5 求m = ？
c = "cidb~c4wvqZvq`<$$x"
key = 5

m = ''.join(chr(ord(char) ^ key) for char in c)
print(m)