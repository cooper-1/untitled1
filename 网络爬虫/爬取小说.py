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

def novel_url(url):
    try:  # 捕获异常
        agent = random.choice(list1)  # 随机选一个user-agent
        header = {"User-Agent": agent}
        proxy = random.choice(proxylist)  # 随机选一个ip地址
        res = requests.post(url, headers=header,proxies=proxy,timeout=10)
        print('第一次·网络状态码： ',res.status_code)
        #print(res.content.decode('utf-8'))
        pattern = re.compile('id="A3" href="(.*?)"', re.S)  # id="A3" href="
        result = pattern.findall(res.text)
        url='https://www.dusuu.com'+result[0]

        pattern = re.compile('<div id="content">(.*?)<div class="bottem2">', re.S)  # class="preview" href=
        result = pattern.findall(res.text)
        print(result)
        result=str(result)
        pattern = re.compile('<p>(.*?)</p>', re.S)  # class="preview" href=
        result = pattern.findall(result)

        print(result)
        global i
        i=i+1
        for type in result:
            path = r'E:\小说\小说'

            filename = path + '/' + 'novel1'+ '   .docx'

            type=str(type)
            with open(filename, 'a',encoding='utf-8') as f:
                f.write(type)

                f.write('\n')
        print('第%s次保存小说成功'%i)
        print(url)
        return url

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
if __name__ == '__main__':
    url = 'https://www.dusuu.com/ml/7726/2607989.html'
    for x in range(1,100):
        time.sleep(2)
        url=novel_url(url)