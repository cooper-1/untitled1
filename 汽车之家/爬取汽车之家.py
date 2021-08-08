# -*-coding:  UTF-8
# @Time    :  2021/8/7 16:06
# @Author  :  Cooper
# @FileName:  爬取汽车之家.py
# @Software:  PyCharm
from bs4 import BeautifulSoup
from agency.requ import getlist

url1 = 'https://car.autohome.com.cn/pic/series/385-1.html#pvareaid=2042220'
response = getlist(url1)
# html = etree.HTML(response)
# print(response)
# result = html.xpath('//ul/li/a/img[@src]')
# print(result)
img = BeautifulSoup(response, 'html.parser')
t1 = img.find_all('img')
for t2 in t1:
    t3 = t2.get('src')
    print(t3)
