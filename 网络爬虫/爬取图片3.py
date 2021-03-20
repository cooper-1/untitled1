# -*-coding:  utf-8 -*-
# @Time    :  2020/12/24 15:21
# @Author  :  Cooper
# @FileName:  爬取图片3.py
# @Software:  PyCharm

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import time
import json
import os
import socket
import os
import re
import urllib
import _json
import random

# 设置请求超时时间，防止长时间停留在同一个请求
socket.setdefaulttimeout(8)

i=0	#用来计数

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

#keyword = input("请输入搜索图片关键字:")#日本网站罗马音名字
keyword = 'Yukino'#日本网站罗马音名字Kasumigaoka
for x in range(1,10):
	proxy = random.choice(proxylist)  # 随机选一个ip地址
	agent=random.choice(list1)  	#随机选一个user-agent
	header={"User-Agent":agent}		#随机选一个user-agent

	keyword = urllib.parse.quote(keyword)#URL只容许一部分ASCII字符，其余字符（如汉字）是不符合标准的，此时就要进行编码
	url="https://wallhaven.cc/search?q={}&page={}".format(keyword,x)#+keyword+"&page={}".format(x)
	res=requests.get(url,proxies=proxy,headers=header)
	print('第%s轮，第一次·网络状态码： '%x,res.status_code)

	#print(res.content.decode('utf-8'))#data-src
	pattern=re.compile('class="preview" href="(.*?)"', re.S)#class="preview" href=
	result=pattern.findall(res.text)
	print(result)
	for url in result:
		res = requests.get(url, proxies=proxy, headers=header)
		print('第%s轮，第二次·网络状态码： '%x, res.status_code)

		pattern = re.compile('id="wallpaper" src="(.*?)"', re.S)
		result = pattern.findall(res.text)
		print(result)
		for url in result:
			path = r'E:\高清图片\1图片'
			i=i+1
			filename = path + '/' + keyword   + str(i) + '   .jpg'
			print('准备保存图片·')
			with open(filename, 'wb') as f:
				try:#捕获异常
					f.write(requests.get(url, proxies=proxy, headers=header,timeout=10).content)
				except HTTPError:
					print('httperror')
				except RequestException:
					print('reqerror')
				except ReadTimeout:
					print('time out')

			print('第%s张图片保存成功' % i, url)