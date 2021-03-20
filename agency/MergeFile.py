# -*-coding:  utf-8 -*-
# @Time    :  2021/2/3 20:31
# @Author  :  Cooper
# @FileName:  MergeFile.py
# @Software:  PyCharm
# -*-coding:  utf-8 -*-

import os

# 字节bytes转化kb\m\g
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

        # return "%fkb" % (kb)
    return "%f" % (kb)

# 获取文件大小
def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return formatSize(size)
    except Exception as err:
        print(err)

# 获取文件夹大小
def getFileSize(path):
    sumsize = 0
    try:
        filename = os.walk(path)
        for root, dirs, files in filename:
            for fle in files:
                size = os.path.getsize(path + fle)
                sumsize += size
        return formatSize(sumsize)
    except Exception as err:
        print(err)

def merge(path,name):
    tuples = os.walk(path)
    for a, b, c in tuples:
        print(len(c))

        filename2 = path + '/' + name+ '.ts'

        with open(filename2, 'wb+') as f:
            for i in range(1, len(c)):
                filename = path + '/' + str(i) + '.ts'
                #print(filename)
                if os.path.exists(filename):
                    f.write(open(filename, 'rb').read())
                else:
                    continue
        print("合并完成！！")

def delete(path):
    j=0
    tuples = os.walk(path)
    for a, b, c in tuples:
        print(len(c))
        for f in c:
            # print(f)
            filename = path + '/' + f
            #print(filename)
            if os.path.exists(filename):
                if float(getDocSize(filename)) <= 2048:
                    os.remove(filename)
                    j = j + 1
                    print('删除文件成功%s' % j)
            else:
                continue
    print('删除文件成功')

if __name__ == "__main__":
    j=0
    path = r'E:\视频\加密电影'
    filename='all9'
    merge(path,filename)
    delete(path)


