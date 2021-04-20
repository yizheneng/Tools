import os
from PIL import Image

threshold = 200
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

for root, dirs, files in os.walk("C:/Users/bing/Desktop/wather_png"):
    for f in files:
        print(os.path.join(root, f))
        img=Image.open(os.path.join(root, f))
        w, h = img.size
        img.thumbnail((w/2,h/2))
        img = img.convert('L')
        img = img.point(table, '1')
        img.save(os.path.join("C:/Users/bing/Desktop/wather_bmp", f.lower().replace(".jpg", "") + ".bmp"), 'bmp')