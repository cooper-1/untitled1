# -*-coding:  utf-8 -*-
# @Time    :  2020/12/23 21:19
# @Author  :  Cooper
# @FileName:  爬取图片.py
# @Software:  PyCharm

import requests
from bs4 import BeautifulSoup
import time
import json
import os
import socket

# 设置请求超时时间，防止长时间停留在同一个请求
socket.setdefaulttimeout(8)
import requests
import os
import re
from bs4 import BeautifulSoup
import random
import time
import urllib
import json,_json



i=0	#用来计数
y=0	#用来计数
#代理ip，针对反爬虫机制
proxylist=[
	{"http":"http://175.43.130.154:9999"},
	{"http":"http://183.166.20.129:9999"},
	{"http":"http://106.110.195.3:9999"},
	{"http":"http://175.44.108.75:9999"},
	{"http":"http://49.86.26.166:9999"},
	{"http":"http://113.121.37.248:9999"}
]
proxy=random.choice(proxylist)#随机选一个ip地址

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



keyword = input("请输入搜索图片关键字:")#日本网站罗马音名字
for x in range(1,5):
	proxy = random.choice(proxylist)  # 随机选一个ip地址
	agent=random.choice(list1)  	#随机选一个user-agent
	header={"User-Agent":agent}		#随机选一个user-agent
	#html="https://anime-pictures.net/pictures/view_posts/"+str(x)+"?search_tag=katou%20megumi&order_by=date&ldate=0&lang=en"

	#keyword = 'Rem'
	keyword = urllib.parse.quote(keyword)#URL只容许一部分ASCII字符，其余字符（如汉字）是不符合标准的，此时就要进行编码
	url="https://wallhaven.cc/search?q={}&page={}".format(keyword,x)#+keyword+"&page={}".format(x)
	res=requests.get(url,proxies=proxy,headers=header)
	print('网络状态码： ',res.status_code)

	#print(res.content.decode('utf-8'))#data-src
	pattern=re.compile('data-src="(.*?)" .*?', re.S)# 取匹配结果的时候，括号中的表达式匹配到的内容可以被单独得到,非贪婪模式
	'''re模块中包含一个重要函数是compile(pattern [, flags]) ，该函数根据包含的正则表达式的字符串创建模式对象。
	可以实现更有效率的匹配。在直接使用字符串表示的正则表达式进行search,match和findall操作时，
	python会将字符串转换为正则表达式对象。
	而使用compile完成一次转换之后，在每次使用模式的时候就不用重复转换。当然，使用re.compile()函数进行转换后，re.search(pattern, string)的调用方式就转换为 pattern.search(string)的调用方式。'''
	'''“.”的作用是匹配除“\n”以外的任何字符，也就是说，它是在一行中进行匹配。这里的“行”是以“\n”进行区分的。a字符串有每行的末尾有一个“\n”，
	不过它不可见。如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。
而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。'''
	#pattern=re.compile("http://(?!(\\.jpg|\\.png)).+?(\\.jpg|\\.png)")
	result=pattern.findall(res.text)#compile()与findall()一起使用，返回一个列表。
	#print(result)
	for url in result:
		print('第%s张图片保存成功'%i,url)

		path = r'D:\工具软件\python3.8\untitled1\爬取图片\图片\图片'
		i=i+1
		filename = path  + '/' +keyword+ str(i) + '.jpg'
		with open(filename, 'wb') as f:
			f.write(requests.get(url).content)


