# -*-coding:  utf-8 -*-
# @Time    :  2020/12/25 13:00
# @Author  :  Cooper
# @FileName:  爬取短视频.py
# @Software:  PyCharm
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import time
import json
import socket
import os
import re
import urllib

import random

i = 0

#代理ip，针对反爬虫机制
proxylist=[
	{"http":"http://175.43.130.154:9999"},
	{"http":"http://183.166.20.129:9999"},
	{"http":"http://106.110.195.3:9999"},
	{"http":"http://175.44.108.75:9999"},
	{"http":"http://49.86.26.166:9999"},
	{"http":"http://113.121.37.248:9999"}
]

#请求头，针对反爬虫机制
agent1="Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"  #谷歌
agent2="Mozilla/5.0 (Windows NT 6.1; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"	#360
agent3="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1;\
 WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5\
 .30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; \
 .NET4.0E; QQBrowser/7.0.3698.400)"											#qq
agent4="Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 \
(KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"		#搜狗
agent5="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36"	#UC
agent6="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"	#火狐
list1=[agent1,agent2,agent3,agent4,agent5,agent6]

for page in range(1,100):
    try:  # 捕获异常
        url = 'https://api-tinyvideo-web.yy.com/home/tinyvideosv2'
        params = {
            'data': '{"uid":0,"page":%s,"pageSize":10}' % str(page)
        }
        agent = random.choice(list1)  # 随机选一个user-agent
        header = {"User-Agent": agent}
        proxy = random.choice(proxylist)  # 随机选一个ip地址
        res = requests.get(url, headers=header,proxies=proxy,timeout=10)
        print('第%s次·网络状态码：'%page,res.status_code)
        print(res.content.decode('utf-8'))
        pattern = re.compile('"resurl":"(.*?)"', re.S)  # id="A3" href="
        result = pattern.findall(res.text)
        #pattern= re.compile('"username":"(.*?)"', re.S)  # id="A3" href="
        #username = pattern.findall(res.text)
        print(result)
        #print(username)

        for url in result:
            agent = random.choice(list1)  # 随机选一个user-agent
            header = {"User-Agent": agent}
            proxy = random.choice(proxylist)  # 随机选一个ip地址

            path = r'E:\小说'
            filename = path + '/' + str(i)+ '   .mp4'

            print('视频·保存中')
            with open(filename,  mode='wb') as f:
                f.write(requests.get(url=url,headers=header,timeout=10).content)
            i = i + 1
            print('第',i,'个视频保存完成')

    except HTTPError:
            print('httperror')
    except RequestException:
            print('reqerror')
    except ReadTimeout:
            print('time out')