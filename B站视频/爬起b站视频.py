# -*-coding:  utf-8 -*-
# @Time    :  2021/1/31 15:37
# @Author  :  Cooper
# @FileName:  爬起b站视频.py
# @Software:  PyCharm
import sys

from you_get import common as you_get #导入you-get库

def info(url):
    sys.argv = ['you-get','-i',url]
    you_get.main()
directory = "E:\视频" #设置下载目录sys.argv = ['you-get', '-o', directory, url]  # sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录
url = input("输入视频网址（url）：\n")
# i = input("输入（1.直接下载/2.选择清晰度）：")
i = '1'
if i == '1':
    sys.argv = ['you-get', '--playlist','-o', directory, url]  # sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录。
    #sys.argv = ['you-get', '-o', directory, url]  # sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录
elif i == '2':
    info(url)
    a = input("输入format：")
    sys.argv = ['you-get','--format='+a,url,'-o',directory]  # 指定下载清晰度（format参数）
    #you-get --playlist  -o E:\MyVedio https://www.bilibili.com/bangumi/play/ss2514/?from=search&seid=5912598083158202353
you_get.main()
