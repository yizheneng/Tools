import os
from PIL import Image
imageSize = (32, 32)
threshold = 200
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

numberStr = "uint8_t picture%dX%d[][] = {\r\n"%imageSize
for root, dirs, files in os.walk("C:/Users/bing/Desktop/wather_png1"):
    for f in files:
        # print(os.path.join(root, f))
        img=Image.open(os.path.join(root, f))
        w, h = img.size
        img.thumbnail(imageSize)
        img = img.convert('L')
        img = img.point(table, '1')
        img.save(os.path.join("C:/Users/bing/Desktop/wather_bmp", f.lower().replace(".jpg", "") + ".bmp"), 'bmp')
        numberStr += "  {"

        w1, h1 = img.size
        for y in range(h1):
            bitCount = 0
            tempByte = 0
            for x in range(w1):
                pixel = img.getpixel((x, y)) 
                if pixel == 0:
                    tempByte = tempByte | (1 << bitCount)
                else:
                    tempByte = tempByte | (0 << bitCount)
                
                bitCount = bitCount + 1
                if bitCount > 7 :
                    numberStr = numberStr + hex(tempByte) + ", "
                    bitCount = 0
                    tempByte = 0 
        numberStr = numberStr[:-2]
        numberStr = numberStr + "}, // " + f + "\r\n"
    numberStr = numberStr + "}"
print(numberStr)