# -*-coding:  utf-8 -*-
# @Time    :  2021/3/12 19:04
# @Author  :  Cooper
# @FileName:  test9.py
# @Software:  PyCharm
# -*-coding:  utf-8 -*-
# @Time    :  2021/3/7 14:28
# @Author  :  Cooper
# @FileName:  test2.py
# @Software:  PyCharm

import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import re
import random
from selenium import webdriver
import time

i=1

user_agent_list = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    ": Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
proxylist=[{"https":"https://121.37.162.236:7749"},	{"http":"http://121.37.162.236:8864"},]

def qudong(url):

    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"')
    driver = webdriver.Chrome(chrome_options=options)
    # options = webdriver.ChromeOptions()
    # user_ag='MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; '+'CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    # options.add_argument('user-agent=%s'%user_ag)
    # driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(15)
    pattern = re.compile(r'>来自</span><style t(.*?)试读已结束， 剩余0页未读', re.S)
    result = pattern.findall(driver.page_source)
    result = re.findall(r'[\u4e00-\u9fa5]+', result[0])
    with open('baidu.txt', 'w') as f:
        for index, item in enumerate(result):
            if index % 11 == 0: f.write('\n')
            f.write('  ' + item)
    # driver.quit()
def getlist1( url = 'https://search.bilibili.com/article?keyword=p%E7%AB%99'):
    # 获取列表URL


        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res=requests.get(url,headers=header,timeout=20)
        print('第%s轮，第一次·网络状态码: '%i,res.status_code)
        print(res.content.decode('utf-8'))
        pattern = re.compile(r'[\u4e00-\u9fa5]+', re.S)  # <img class="" src=
        result = pattern.findall(res.text)
        print(result)
        # for url in result[:1]:
        #     url='https:'+url
        #     print(url)

if __name__ == "__main__":
    url='https://live.kuaishou.com/u/kuaishouwzry'
    # getlist1(url)
    qudong(url)
