#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 加密解密模块
from Crypto.Cipher import AES
# sys模块，用于获得命令行参数
import sys
# 正则表达式模块
import re

# 获得key值
key = "706ad7229ebbe8ce"
# 根据key创建解密对象，python3中使用encode将str转为bytes，否则报错
cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, key.encode('utf-8'))
# 首先打开大视频
count = 0
with open("1.mp4", 'ab') as file:
    while True:
        count = count + 1
        with open("downloaded/%d.ts" % count, 'rb') as inf:
            data = inf.read()
            print(len(data))
            if (len(data) <= 0):
                exit()
            file.write(cryptor.decrypt(data))
