# -*-coding:  UTF-8
# @Time    :  2021/7/18 15:38
# @Author  :  Cooper
# @FileName:  测试requ.py
# @Software:  PyCharm

from agency.requ import getlist

a = getlist('https://search.bilibili.com/article?keyword=p%E7%AB%99')
print(a)
