# -*-coding:  UTF-8
# @Time    :  2021/5/23 15:47
# @Author  :  Cooper
# @FileName:  使用xpath爬取当当网.py
# @Software:  PyCharm


from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# import os,sys,io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
options = webdriver.ChromeOptions()
options.headless = True  # 设置选项为无界面
options.add_argument(
    'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(options=options)
driver.get("http://search.dangdang.com/?key=python&act=input")
time.sleep(2)
# print(driver.page_source.encode('gbk'))
# f = open("out.html","w",encoding='utf-8')
# f.write(driver.page_source)
# f.close()

html = etree.HTML(driver.page_source)
result = html.xpath("//p[@class='name']/a/text()")
print(result)
result = html.xpath("//p[@class='name']/a/@title")
print(result)
print('-'*100)
result = html.xpath("//p[@class='name']/a")[1].text
print(result)
# result = html.xpath("//p[@class='name']/a]")
# print(result)
driver.quit()