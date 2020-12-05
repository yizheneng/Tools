#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#加密解密模块
from Crypto.Cipher import AES
#sys模块，用于获得命令行参数
import sys
#正则表达式模块
import re

#argv[1]:m3u8文件路径
#默认m3u8文件和视频数据文件夹应该在同一路径下
#key文件在数据文件夹中

with open(sys.argv[1]) as m3u8:
    list=[]
    keyp=absp=datadir=None
    while 1:
        line = m3u8.readline()
        if re.match('#EXT-X-KEY',line) != None:
            #正则表达式替换，获得key文件的路径
            keyp='.'+re.sub('#EXT-X-KEY.*(/[^/]+/\w+)"','\g<1>',line)
            #不知道为什么路径前面有空格，要去除
            keyp=re.sub('\s|\n','',keyp)
            #匹配获得绝对路径
            absp=re.sub('#EXT-X-KEY.*?"(/.*/).*"','\g<1>',line)
            #不知道为什么路径前面有空格，要去除
            absp=re.sub('\s|\n','',absp)
            #获得数据文件夹名字:“./xxx/”的形式
            datadir=re.sub('(\./\w+/)\w+','\g<1>',keyp)
            print(keyp,absp,datadir)
            #break
        if keyp and absp and re.match(absp,line):
            #去除路径前缀
            name=re.sub(absp,'',line)
            #去除文件末尾的\n
            name=re.sub('\n','',name)
            #所有小视频名列表
            list.append(name)
        if not line:
            break
#print(list)
#上面就获得了key和所有文件的路径，然后开始解密

#获得key值
with open(keyp) as keyfp:
    key=keyfp.read()
#根据key创建解密对象，python3中使用encode将str转为bytes，否则报错
cryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC,key.encode('utf-8'))
#首先打开大视频
with open(re.sub('.m3u8','.mp4',sys.argv[1]), 'ab') as file:
    #循环对每个小视频解密并合并到大视频中
    for i in list:
        with open(datadir+i, 'rb') as inf:
            data=inf.read()
        file.write(cryptor.decrypt(data))