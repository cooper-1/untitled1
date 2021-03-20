# -*-coding:  utf-8 -*-
# @Time    :  2020/12/16 14:56
# @Author  :  Cooper
# @FileName:  网络爬虫261.py
# @Software:  PyCharm
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException

#url='https://httpbin.org/post/'
url='https://www.baidu.com/'
#url='https://www.mingrisoft.com/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
proxy={'http':'175.42.68.184 :9999'}
data={'name':'cooper'}
response=requests.post(url,headers=headers,proxies=proxy,data=data)
#print('以字节流形式打印网页源码',response.content.decode('utf-8'))
print('以字节流形式打印网页源码',response.headers)
