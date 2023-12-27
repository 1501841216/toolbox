# 导入 PIL 库
from PIL import Image
import math

def extract_rgb_values(rgb_string):
    rgb_string = rgb_string.strip("()")
    r, g, b = map(int, rgb_string.split(","))
    return r, g, b

pixel_num = 135000
for i in range(1, int(math.sqrt(pixel_num)) + 1):
    if pixel_num % i == 0:
        width = i
        height = pixel_num//i
        print(width, height)
        # 创建 Image 对象
        image = Image.new("RGB",(height,width))
        # 获取画布
        pixels = image.load()
        home = "E:\\CTF\\CTFQD\\2023ynyc\\misc\\"
        f = open(home + "basic.txt")
        data = f.read().split('\n')
        count = 0
        for y in range(image.height):
            for x in range(image.width):
                r,g,b = extract_rgb_values(data[count])
                pixels[x,y] = (r,g,b)
                count += 1
        image.show()