# -*-coding:  utf-8 -*-
# @Time    :  2020/12/15 22:05
# @Author  :  Cooper
# @FileName:  网络爬虫2.py
# @Software:  PyCharm
import urllib3
import sys
import urllib
#创建PoolManager对象，用于处理与线程池的连接及线程安全的所有细节
http=urllib3.PoolManager()
#对需要爬取的网页发送请求
# response=http.request('GET','http://www.baidu.com')
# print(response.data.decode())
response=http.request('POST','http://httpbin.org/post',fields={'word':'hellow'})
print(response.data.decode())