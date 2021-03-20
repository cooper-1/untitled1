# -*-coding:  utf-8 -*-
# @Time    :  2020/12/18 13:22
# @Author  :  Cooper
# @FileName:  爬虫35.py
# @Software:  PyCharm
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException

url='http://httpbin.org/post'
#url='http://httpbin.org/get'
#url='https://www.baidu.com/'
#url='https://www.mingrisoft.com/'
key_dict={'key1':'value1','key2':'value2'}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
proxy={'http':'175.42.68.184 :9999'}
#response=requests.get(url,params=key_dict,headers=headers,proxies=proxy)#get方法要对应#url='http://httpbin.org/get'
response=requests.post(url,data=key_dict)#POST方法要对应#url='http://httpbin.org/get'
print('以字节流形式打印网页源码',response.content.decode('utf-8'))