# -*-coding:  utf-8 -*-
# @Time    :  2021/1/25 19:44
# @Author  :  Cooper
# @FileName:  b站弹幕.py
# @Software:  PyCharm

# -*-coding:  utf-8 -*-
# @Time    :  2020/12/16 14:56
# @Author  :  Cooper
# @FileName:  网络爬虫261.py
# @Software:  PyCharm
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException

#url='https://httpbin.org/post/'
url='https://search.bilibili.com/all?keyword=%E5%88%BA%E5%AE%A2%E4%BC%8D%E5%85%AD%E4%B8%83&from_source=nav_suggest&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.10'
#url='https://www.mingrisoft.com/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
proxy={'http':'175.42.68.184 :9999'}
data={'name':'cooper'}
response=requests.get(url,headers=headers,proxies=proxy)
#print('以字节流形式打印网页源码',response.content.decode('utf-8'))
print('以字节流形式打印网页源码',response.text)
