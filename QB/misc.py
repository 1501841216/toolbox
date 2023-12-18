# 导入 PIL 库
from PIL import Image
# 创建 Image 对象
image = Image.new("RGB",(100,100))
# 获取画布
pixels = image.load()
home = "E:\\CTF\\CTFQD\\2023ynyc\\misc\\"
f = open(home + "basic.txt")
data = f.read()
for i in data:
    print(i)
for y in range(image.height):
    for x in range(image.width):
        r = i[0]
        g = i[1]
        b = i[2]
        pixels[x,y] = (r,g,b)




image.save("picture.png")