# -*-coding:  utf-8 -*-
# @Time    :  2020/12/15 21:36
# @Author  :  Cooper
# @FileName:  网络爬虫.py
# @Software:  PyCharm
import urllib.request
import urllib.parse


#将数据使用urlencode编码处理后，再使用,encoding设置为'utf-8'编码
data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
#打开指定需要爬取的网页
# response=urllib.request.urlopen('http://www.baidu.com')
# html1=response.read()#读取网页代码
# print(html1)#打印读取内容
response1=urllib.request.urlopen('http://httpbin.org/post',data=data)
html=response1.read()#读取网页代码
print(html)#打印读取内容