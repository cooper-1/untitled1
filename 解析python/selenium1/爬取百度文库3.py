# -*-coding:  utf-8 -*-
# @Time    :  2021/3/10 20:24
# @Author  :  Cooper
# @FileName:  爬取百度文库3.py
# @Software:  PyCharm
from selenium import webdriver
import time
import re
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://wenku.baidu.com/view/9816e4ed5122aaea998fcc22bcd126fff7055d86.html")
time.sleep(15)
print(driver.page_source)#打印页面源码
pattern = re.compile(r'>来自</span><style t(.*?)试读已结束， 剩余0页未读', re.S)
result = pattern.findall(driver.page_source)
print(result[0])
pattern = re.compile(r'[\u4e00-\u9fa5]+', re.S)
result = pattern.findall(result[0])
print(result)
with open('baidu.txt','w') as f:
    for index,item in enumerate(result):
        if index%11==0:f.write('\n')
        f.write('  '+item)
driver.quit()