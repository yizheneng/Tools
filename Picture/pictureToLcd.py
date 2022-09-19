import os
from PIL import Image
imageSize = (64, 64)
threshold = 200
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

numberStr = "const uint8_t picture%dX%d[][%d] = {\r\n"%(imageSize[0], imageSize[1], imageSize[0]*imageSize[1]/8)
for root, dirs, files in os.walk("C:/Users/bing/Pictures/1"):
    for f in files:
        # print(os.path.join(root, f))
        img=Image.open(os.path.join(root, f))
        w, h = img.size
        img.thumbnail(imageSize)
        img = img.convert('L')
        img = img.point(table, '1')
        img.save(os.path.join("C:/Users/bing/Pictures/2", f.lower().replace(".jpg", "") + ".bmp"), 'bmp')
        numberStr += "  {"

        w1, h1 = img.size

        # for y in range(h1):
        #     bitCount = 0
        #     tempByte = 0
        #     for x in range(w1):
        #         pixel = img.getpixel((x, y)) 
        #         if pixel == 0:
        #             tempByte = tempByte | (1 << bitCount)
        #         else:
        #             tempByte = tempByte | (0 << bitCount)
                
        #         bitCount = bitCount + 1
        #         if bitCount > 7 :
        #             numberStr = numberStr + hex(tempByte) + ", "
        #             bitCount = 0
        #             tempByte = 0

        tempY = int(h1 / 8)
        for y in range(tempY):
            tempByte = 0
            for x in range(w1):
                for i in range(8):
                    pixel = img.getpixel((x, y * 8 + i)) 
                    if pixel == 0:
                        tempByte = tempByte | (1 << i)
                    else:
                        tempByte = tempByte | (0 << i)

                numberStr = numberStr + hex(tempByte) + ", "
                tempByte = 0 

        numberStr = numberStr[:-2]
        numberStr = numberStr + "}, // " + f + "\r\n"
    numberStr = numberStr + "};"
print(numberStr)

file_handle=open('weathericon.h',mode='w')
file_handle.write(numberStr)
