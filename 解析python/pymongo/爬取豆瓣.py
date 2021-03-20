# -*-coding:  utf-8 -*-
# @Time    :  2021/2/19 20:04
# @Author  :  Cooper
# @FileName:  爬取豆瓣.py
# @Software:  PyCharm

import requests,re
import time
from pymongo import *
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import random

url='https://movie.douban.com/top250?start='
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

proxy={'http':'175.42.128.139 :9999'}
movie_list=[]

for i in range(0,1):
    #time.sleep(2)
    header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
    url = "https://movie.douban.com/top250?start=" +str(i*25)+'&filter='
    res=requests.get(url, timeout=30, headers=header)
    res.raise_for_status()

    print('第 '+str(i+1)+' 页响应状态码：',res.status_code)
    pattern = re.compile('<li>(.*?)</li>', re.S)  # <img class="" src=
    result = pattern.findall(res.text)
    # print(result)
    for data in result:
        # print(data)
        pattern = re.compile('<span class="title">(.*?)</span>', re.S)  # <img class="" src=
        title = pattern.findall(data)[0]
        print(title)
        pattern = re.compile('<span class="rating_num" property="v:average">(.*?)</span>', re.S)  # <img class="" src=
        score = pattern.findall(data)[0]
        print(score)
        pattern = re.compile('<a href="(.*?)">', re.S)  # <img class="" src=
        link = pattern.findall(data)[0]
        print(link)
        movie_list.append({'电影':title,'评分':score,'链接':link})
print(movie_list)
client=MongoClient()
db=client.spider#创建数据库
collection=db.movie250#创建集合
# collection.insert_many (movie_list)#插入多条数据
cursor=collection.find({'评分':'9.4'})
# print(cursor)
for data in cursor:
    print(data)
