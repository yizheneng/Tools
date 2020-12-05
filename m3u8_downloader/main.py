import os
from concurrent.futures import ThreadPoolExecutor

fileHandle = open("downList.m3u8", 'r')
count = 0
fileUrlList = []

while True:
    line = fileHandle.readline()
    if len(line) <= 0:
        break
    if line[0] == '#':
        continue
    fileUrlList.append(line.replace('\n', ''))

print(len(fileUrlList))


def downWithFileUrlAndIndex(fileUrl, index):
    # if line.__contains__("http"):
    #     count = count + 1
    cmd = "wget %s -O downloaded/%d.ts" % (fileUrl, index)
    print("cmd: %s" % cmd)
    os.system(cmd)


if __name__ == '__main__':
    threadPool = ThreadPoolExecutor(max_workers=80, thread_name_prefix="test_")
    for i in range(0, len(fileUrlList)):
        future = threadPool.submit(downWithFileUrlAndIndex, fileUrlList[i], i + 1)

    threadPool.shutdown(wait=True)
