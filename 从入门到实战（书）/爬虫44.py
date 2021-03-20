# -*-coding:  utf-8 -*-
# @Time    :  2020/12/18 20:50
# @Author  :  Cooper
# @FileName:  爬虫44.py
# @Software:  PyCharm
import requests
import requests,re
import json
from requests.exceptions import ReadTimeout,HTTPError,RequestException
from bs4 import BeautifulSoup

url='http://www.santostang.com/2018/07/04/hello-world/'

key_dict={'key1':'value1','key2':'value2'}
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

response=requests.get(url,headers=headers)
print(' 页响应状态码：',response.status_code)
json_data=json.loads(response.text)
# comment_list=json_data['data']['comment']
# message=comment_list[eachone]['content']
# print(message)
# print(response.content.decode('utf-8'))
