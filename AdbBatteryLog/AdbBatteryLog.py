# encoding:utf-8
import os, time


def get_battery_info():
    result = os.popen("adb shell dumpsys battery").read()
    level = 0
    voltage = 0.0
    current = 0.0

    for line in result.splitlines():
        if line.__contains__("level"):
            level = int(line.split(":")[1])
        if line.__contains__("voltage"):
            voltage = float(line.split(":")[1])
        if line.__contains__("current"):
            current = float(line.split(":")[1])
    return level, voltage, current


fd = os.open(time.strftime(os.path.expanduser('~') + "\\Desktop\\battery_log\\battery_%Y_%m_%d__%H%M%S",
                           time.localtime()) + ".csv", os.O_CREAT | os.O_WRONLY)
os.write(fd, "time,level,voltage,current\r\n".encode("UTF-8"))
while True:
    level, voltage, current = get_battery_info()
    batteryStr = "%s,%d,%f,%f\r\n" % (time.strftime("%m_%d_%H%M%S", time.localtime()), level, voltage, current)
    print(batteryStr)
    os.write(fd, batteryStr.encode("UTF-8"))
    time.sleep(1)
