# -*-coding:  utf-8 -*-
# @Time    :  2021/1/2 13:38
# @Author  :  Cooper
# @FileName:  b站图片.py
# @Software:  PyCharm

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import time
import os
import re
import urllib
import random

i = 0

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


def downloading(url):
    try:  # 捕获异常
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        proxy = random.choice(proxylist)  # 随机选一个ip地址
        res = requests.get(url, headers=header,proxies=proxy,timeout=10)
        print('第%s次·第一次网络状态码：'%page,res.status_code)
        #print(res.content.decode('utf-8'))
        pattern = re.compile('class="article-item"><a href="(.*?)"', re.S)
        result = pattern.findall(res.text)
        print(result)

        list1 = []
        for url in result:
            list1.append('https:'+url)
        print(list1)
        for url in list1:
            res = requests.get(url, headers=header, proxies=proxy, timeout=10)
            print('第%s次·第二网络状态码：' % page, res.status_code)
            pattern = re.compile('img data-src="(.*?)"', re.S)  # class="preview" href=
            result = pattern.findall(res.text)
            print(result)

            list2 = []
            for url in result:
                list2.append('https:' + url)
            print(list2)

        for url in list2[1:-1]:
            path = r'E:\B站\美图2'
            global i
            i = i + 1
            d=url.split('.')[-1]
            filename = path + '/' + str(i) + '.'+str(d)
            print('第%s次准备保存图片·'%i,url)

            with open(filename, 'wb') as f:
                f.write(requests.get(url, proxies=proxy, headers=header, timeout=10).content)

    except HTTPError:
            print('httperror')
    except RequestException:
            print('reqerror')
    except ReadTimeout:
            print('time out')


if __name__ == '__main__':
    for page in range(1, 10):
        url = 'https://search.bilibili.com/article?keyword=p%E7%AB%99&page={}'.format(page)
        downloading(url)