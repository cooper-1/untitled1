# -*-coding:  utf-8 -*-
# @Time    :  2020/12/16 13:20
# @Author  :  Cooper
# @FileName:  网络爬虫259.py
# @Software:  PyCharm
import requests
url='http://www.baidu.com/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
response=requests.get(url,headers=headers)
print('打印状态码',response.status_code)#200状态码：表示请求已成功，请求所希望的响应头或数据体将随此响应返回
print('打印请求URL',response.url)
print('打印头部信息',response.headers)
print('以字节流形式打印网页源码',response.content.decode('utf-8'))