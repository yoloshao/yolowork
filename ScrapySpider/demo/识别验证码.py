import subprocess
import os
from PIL import Image


def image_to_string(img):
    """
    把图片转化为字符串
    """
    filename = os.path.splitext(img)[0]
    subprocess.call('tesseract {img} {filename}'.format(img=img, filename=filename), shell=True)
    with open(filename + '.txt') as f:
        text = f.read().strip()
    return text

image = Image.open('douban.jpg')
c = image.convert('L')
c.save('c.jpg')

# 0 黑色
# 255 白色

# 20 黑白的临界值
# 获得所有像素
pixels = c.load()
for x in range(c.width):
    for y in range(c.height):
        if pixels[x, y] < 5:
            pixels[x, y] = 0
        else:
            pixels[x, y] = 255
c.save('c.jpg')

result = image_to_string('c.jpg')
strings = result.split()
print(strings)
print(max(strings))