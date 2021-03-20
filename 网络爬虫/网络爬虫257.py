# -*-coding:  utf-8 -*-
# @Time    :  2020/12/15 23:57
# @Author  :  Cooper
# @FileName:  网络爬虫257.py
# @Software:  PyCharm
import requests

response=requests.get('http://www.baidu.com/')
print('打印状态码',response.status_code)#200状态码：表示请求已成功，请求所希望的响应头或数据体将随此响应返回
print('打印请求URL',response.url)
print('打印头部信息',response.headers)
print('打印cookies信息',response.cookies)
print('以文本形式打印网页源码',response.text)
print('以字节流形式打印网页源码',response.content)
#对要爬取的网页·发送请求
response=requests.post('http://httpbin.org/post',data={'word':'hellow'})#data为表单参数
print('以字节流形式打印网页源码',response.content)#以字节流形式打印网页源码