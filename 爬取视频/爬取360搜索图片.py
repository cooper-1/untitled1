# -*-coding:  utf-8 -*-
# @Time    :  2020/12/25 20:39
# @Author  :  Cooper
# @FileName:  爬取360搜索图片.py
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

y = 0

user_agent_list = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19                                                      *                                   .0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

proxylist=[
	{"http":"http://175.43.130.154:9999"},
	{"http":"http://183.166.20.129:9999"},
	{"http":"http://106.110.195.3:9999"},
	{"http":"http://175.44.108.75:9999"},
	{"http":"http://49.86.26.166:9999"},
	{"http":"http://113.121.37.248:9999"}
]

try:  # 捕获异常
    list = []
    list2 = []
    urls=[]
    url = 'https://image.so.com/j?'
    header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
    proxy = random.choice(proxylist)  # 随机选一个ip地址
    keyword = '特朗普'
    paginator = 2
    keyword = urllib.parse.quote(keyword)  # URL只容许一部分ASCII字符，其余字符（如汉字）是不符合标准的，此时就要进行编码。
    params = []
    for i in range(0,paginator + 1):
        j = 111
        if i > 0:
            j = 60
        print(j)
        params.append(
            'q={}&pd=1&pn=60&correct={}&adstar=0&tab=all&sid=671bb036f4082959c769420d0a208bbe&ras=0&cn=0&gn=0&kn=50&crn=0&bxn=20&cuben=0&pornn=0&manun=50&src=srp&sn={}&ps={}&pc={}'.format(
                keyword, keyword, (130 + 10 * i), (111 + 60 * i), j))
    for x in params:
        urls.append(url + x)
    for url in urls:
        res = requests.get(url, headers=header, proxies=proxy, timeout=10)
        print('第%s次·第一次网络状态码：' % 1, res.status_code)
        print(res.content.decode('utf-8'))
        pattern = re.compile('"thumb":"(.*?)"', re.S)
        result = pattern.findall(res.text)
        print(result)
        for url in result:
            path = r'E:\B站\图片4'
            filename = path + '/' + str(y) + '   .jpg'
            y=y+1
            print(url)
            url=url.replace('\\','')
            print(url)
            print('第%s次准备保存图片·' % y, url)

            with open(filename, 'wb') as f:
                f.write(requests.get(url, proxies=proxy, headers=header, timeout=10).content)


except HTTPError:
    print('httperror')
except RequestException:
    print('reqerror')
except ReadTimeout:
    print('time out')