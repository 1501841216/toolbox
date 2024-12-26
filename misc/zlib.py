import zlib

dir = "F:\\CTF\\dlp\\_dlp-1.png.extracted\\"
with open(dir + '5B.zlib','rb') as f:
    compressed_data=f.read()
    decompressed_data= zlib.decompress(compressed_data)

with open(dir + 'de5B.txt','wb') as f:
    f.write(decompressed_data)