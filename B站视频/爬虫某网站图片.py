#图片等文件爬取全代码
import requests
import os
import re
from bs4 import BeautifulSoup
import random
import time
import urllib



i=0	#用来计数
#代理ip，针对反爬虫机制
proxylist=[
	{"http":"http://175.43.130.154:9999"},
	{"http":"http://183.166.20.129:9999"},
	{"http":"http://106.110.195.3:9999"},
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
list1=[agent1,agent2,agent3,agent4,agent5]

for x in range(0,10):
	agent=random.choice(list1)  	#随机选一个user-agent
	header={"User-Agent":agent}		#随机选一个user-agent
	#html="https://anime-pictures.net/pictures/view_posts/"+str(x)+"?search_tag=katou%20megumi&order_by=date&ldate=0&lang=en"
	keyword = input("请输入搜索图片关键字:")#日本网站罗马音名字
	keyword = urllib.parse.quote(keyword)#URL只容许一部分ASCII字符，其余字符（如汉字）是不符合标准的，此时就要进行编码
	html="https://anime-pictures.net/pictures/view_posts/"+str(x)+"?search_tag="+keyword+"&order_by=date&ldate=0&lang=en"

	res=requests.get(html,proxies=proxy,headers=header)
	#time.sleep(1)					#有了网站地址后向服务器发出请求
	bs=BeautifulSoup(res.text,'lxml')		#运用解析库解析获取的内容

	#通过正则表达式和beautifulsoup的find_all函数获取所有图片的地址,并且以列表形式返回给images
	images=bs.find_all("img",{"src":re.compile(r"\.jpg")})#从compile()函数的定义中，可以看出返回的是一个匹配对象
	#上一行代码可以看成是找到所有的img的东西，然后找到有src的东西,re.compile(r"\.jpg")含有\.jpg分成一个个列表list
	for image in images:					#在列表中循环
		url="https:"+image["src"]
		print(image)
		print(image["src"])
		root=r"D:\工具软件\python3.8\untitled1\爬取图片\图片"   					#需要存储的根目录
		path=root+url.split('/')[-1]  		#需要存储的路径以及文件名，若要自定义文件名则只需将改为path=root+"文件名.jpg"
		try:
			if not os.path.exists(root):  	#查看根目录是否存在，不存在就创建
				os.mkdir(root)
			if not os.path.exists(path):	#查看文件（文件路径)是否存在
				r=requests.get(url,proxies=proxy,headers=header)			#浏览器向服务器发出请求
				#time.sleep(1)
				with open(path,'wb') as f:
					f.write(r.content)		#把获取到的内容以二进制形式写入文件（图片等文件都是二进制存储的）
					#f.close()				#写完后好像with自己会关，这行代码可要可不要
					print("文件保存成功"+str(i))
					i=i+1
			else:
				print("文件已存在"+str(i))
				i=i+1
		except:
			print("爬取失败"+str(i))
			i=i+1
print(i)
