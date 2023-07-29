from Crypto.Util.number import long_to_bytes, bytes_to_long
# Extract lowercase in a string
def extract(string1):
    length = len(string1)
    list1 = []
    for i in range(length):
        # char.isupper for capital letter
        if string1[i].islower():
            list1.append(string1[i])
    return list1


the_dir = "E:\\CTF\\CTFQD\Crypto\\f590c0f99c014b01a5ab8b611b46c57c"
f = open(the_dir + "\\f590c0f99c014b01a5ab8b611b46c57c.txt", "r", encoding='utf-8')
s = ''
for  line in f:
    for c in line:
        if c.isupper():
            s += c
print(s)

# make a table for translation
s2 = s.replace('ZERO', '0').replace('ONE', '1')
print(s2)
print(long_to_bytes(int(s2, 2)))
