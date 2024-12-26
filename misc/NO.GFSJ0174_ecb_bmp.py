# adworld
# NO.GFSJ0174
# openssl salted BMP,ecb encryptd images
# 4K resolution either 3840x2160 or 4096x2160 pixels


from Crypto.Util.number import long_to_bytes

home = 'F:\\CTF\\CTFQD\\Crypto\\c9b973a1f7114c0486b0410536370380\\cry300~\\'
with open(home + 'ecb.bmp','rb') as f:
    data=f.read()

pre = 0x424d76483f00000000007600000028000000000f000070080000010004000000000000483f00000000000000000000000000000000000000000000008000008000000080800080000000800080008080000080808000c0c0c0000000ff0000ff000000ffff00ff000000ff00ff00ffff0000ffffff00ffffffffffffffffffff
out = long_to_bytes(pre)+data[128:]

with open(home + 'out.bmp','wb') as g:
    g.write(out)