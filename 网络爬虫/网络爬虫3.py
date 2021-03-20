# -*-coding:  utf-8 -*-
# @Time    :  2020/12/15 23:39
# @Author  :  Cooper
# @FileName:  网络爬虫3.py
# @Software:  PyCharm
import urllib3
import sys
import urllib
#创建PoolManager对象，用于处理与线程池的连接及线程安全的所有细节
http=urllib3.PoolManager()
#对需要爬取的网页发送请求
response=http.request('POST','http://www.baidu.com',fields={'word':'hellow'})
print(response.data.decode())