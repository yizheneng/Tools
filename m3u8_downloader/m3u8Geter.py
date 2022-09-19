import os
from selenium import webdriver


class M3U8Getter():
    url = ""
    outDir = ""

    def __init__(self, url, outDir): #url 要解析的网址  outDir 输出文件夹
        self.url = url
        self.outDir = outDir

    def startDownload(self):
        if not os.path.exists(self.outDir):
            os.makedirs(self.outDir)

        browser = webdriver.Chrome()
        browser.get(self.url)
        m3u8 = browser.find_elements_by_tag_name("script")
        print(m3u8)


if __name__ == '__main__':
    m3u8ListGetter = M3U8Getter("https://v.608y.com/vplay/142652/0/1.html", "D:/hysxm/")
    m3u8ListGetter.startDownload()

