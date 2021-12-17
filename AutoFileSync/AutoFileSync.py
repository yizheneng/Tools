import os,time

sourceFilePath = "C:\\Users\\bing\\Documents\\Arduino\\projects\\arduino_build\\esp32s2_arduino\\IotS2.ino.bin"
objectPath = "G:\\IotS2.ino.bin"

lastTime = ""
while True:
    if os.path.getmtime(sourceFilePath) != lastTime:
        cmd = "copy %s %s" % (sourceFilePath, objectPath)
        print("File changed,%s!!\r\n"%cmd)
        os.system(cmd)
        lastTime = os.path.getmtime(sourceFilePath)
    time.sleep(1)