# -*-coding:  utf-8 -*-
# @Time    :  2021/3/6 16:22
# @Author  :  Cooper
# @FileName:  网易云2.py
# @Software:  PyCharm
# -*-coding:  utf-8 -*-
# @Time    :  2021/2/21 23:16
# @Author  :  Cooper
# @FileName:  test8.py
# @Software:  PyCharm


import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import re
import random
import urllib3

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

def getlist(url):
    # 获取列表URL
    try:
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res=requests.get(url,timeout=20)
        print('第%s轮，第一次·网络状态码: '%i,res.status_code)
        print(res.content.decode('utf-8'))
        pattern = re.compile('\{"Id"(.*?)},', re.S)  # <img class="" src=
        result = pattern.findall(res.text)
        print(len(result))
        for data in result:
            item = {}
            # 职位名称
            pattern = re.compile('"RecruitPostName":"(.*?)"', re.S)  # <img class="" src=
            title = pattern.findall(data)[0]
            print(title)
            item['title'] = title
            pattern = re.compile('"LocationName":"(.*?)",', re.S)  # <img class="" src=
            location = pattern.findall(data)[0]
            # print(name)
            item['location'] = location
            # pattern = re.compile('<h3>.*<span>(.*?)</span>.*</h3>', re.S)  # <img class="" src=

            pattern = re.compile('"Responsibility":"(.*?)",', re.S)  # <img class="" src=
            describe = pattern.findall(data)[0]
            print(describe)
            item['describe'] = describe
            print(item)


    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == "__main__":

    url = 'https://m701.music.126.net/20210306164535/c20d36229980683b8531edd95749e677/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/5001223529/571f/b008/8363/06f089e5d0dd42f484196f04180f6924.m4a'
    getlist(url)
