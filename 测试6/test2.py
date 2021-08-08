# -*-coding:  UTF-8
# @Time    :  2021/8/7 16:32
# @Author  :  Cooper
# @FileName:  test2.py
# @Software:  PyCharm
from agency.requ import getlist
from lxml import etree

url1 = 'https://search.bilibili.com/article?keyword=p%E7%AB%99'
response = getlist(url1)
html = etree.HTML(response)
print(response)
result = html.xpath('//li/div//div/a[@href]')
print(result)
