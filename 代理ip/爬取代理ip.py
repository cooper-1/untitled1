# -*-coding:  utf-8 -*-
# @Time    :  2021/1/28 20:40
# @Author  :  Cooper
# @FileName:  爬取代理ip.py
# @Software:  PyCharm

from gevent import monkey#把下面有可能有IO操作的单独做上标记
monkey.patch_all()#将IO转换为异步执行的函数
"""也就是说，我们要先引用多协程模块monkey.patch_all()，再引用别的才行，不然会报错"""
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import time
import os
import re
import random
import gevent
from gevent.queue import Queue
import sys
sys.setrecursionlimit(1000000)  # 例如这里设置为一百万
i=0
j = 0
j2 = 0
i2=0
i3=0
i4=0
i5=0
urllist=[]#存取URL的列表
urllist2=[]#存取URL的列表
urllist3=[]#存取URL的列表

user_agent_list=agency.proxies.user_agent_list
proxylist=Proxy().getproxy()

url='https://www.89ip.cn/index_1.html'
header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
proxy = random.choice(proxylist)  # 随机选一个ip地址
res = requests.get(url, headers=header,proxies=proxy,timeout=10)
print('第%s轮，第一次·网络状态码： '%i,res.status_code)
#print(res.content.decode('utf-8'))
#pattern = re.compile('[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}', re.S)  # <img class="" src=
pattern = re.compile('<tr>(.*?)</tr>', re.S)
result=pattern.findall(res.text)
print(result)
for ip in result:
    pattern = re.compile('[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}', re.S)  # <img class="" src=
    #print(ip)
    #pattern = re.compile('<tr>(.*?)</tr>', re.S)
    result = pattern.findall(ip)
    i=i+1
    pattern = re.compile('<td>\n\t\t\t([1-9]{1,4})\t\t</td>', re.S)
    dkh = pattern.findall(ip)
    # if((len(result)!=0) and (len(dkh)!=0)):
    if((result!=[]) and (dkh!=[])):
        print('ip%s=======' % i, result)
        print('端口号%s=======' % i, dkh)