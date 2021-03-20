# -*-coding:  utf-8 -*-
# @Time    :  2021/1/29 20:52
# @Author  :  Cooper
# @FileName:  删除文件.py

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


if __name__ == "__main__":
    j=0
    for i in range(20,25):
        path = r'E:\B站\图片%s'%i
        tuples=os.walk(path)
        for a,b,c in tuples:
            print(len(c))
            for f in c:
                #print(f)
                filename = path + '/' +  f
                #print(filename)
                if os.path.exists(filename):
                        if  float(getDocSize(filename))<=10:
                            os.remove(filename)
                            j=j+1
                            print('删除文件成功%s'%j)
                else:
                    continue
