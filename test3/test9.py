# -*-coding:  utf-8 -*-
# @Time    :  2021/3/18 19:30
# @Author  :  Cooper
# @FileName:  test9.py
# @Software:  PyCharm
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import random

j=0
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
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
cookie={'cookie': 'Hm_lvt_522b01156bb16b471a7e2e6422d272ba=1616054920; UM_distinctid=1784461251381-0a5f2ad4b2ff9b-376b4502-1fa400-17844612514334; login_redirect=; XSRF-TOKEN=eyJpdiI6IkdIeHIyU3p4bk1sOEhJVU5XR3M0QUE9PSIsInZhbHVlIjoiVTNEcitjQUMyZzFJcmNEZEUrRjJFQT09IiwibWFjIjoiYWNlYzg3OWVmYTM5OTNhYjM2NWRhMjg5ZjdiNzNkN2Y3MWEyNzYyYzM1YWZkZGQzZWIwZWQ3M2I2YWI0YTFhNSJ9; laravel_session=eyJpdiI6ImJMSm1xb21FYU9yVGgrakIxUzBsamc9PSIsInZhbHVlIjoiSElBeTkrNThRT1JWeXFPZVFUMk9qS0RFMzNMekdPbVJLUGFJUHA0bm1lWWU5bDF4ZFVaU1hvOVwvMWhTUmZGK3RzcThFdWJlbUhXM1RUYUxoVjZseUx3PT0iLCJtYWMiOiJkNGQ4OGViOGMxYTYyNDg0YWU3NmRlMTc2ZmI5MTljMGFkM2FhM2U1NjEzNWVkMmU3Zjg5MTJhODM5Yjg0ODQ0In0%3D; x-token=; Hm_lpvt_522b01156bb16b471a7e2e6422d272ba=1616068870'}
def getlist(url):
    # 获取列表URL
        global j
        j += 1
        header = {'User-Agent': random.choice(user_agent_list)}
        res=requests.get(url, headers=header,cookies=cookie,timeout=20)
        print('第%s轮，第一次·网络状态码: '%j,res.status_code)
        print('第%s轮，第一次·网络状态码: '%j,res.cookies)
        print(res.content.decode('utf-8'))
        for i in res.cookies:
            print(i)

if __name__ == "__main__":
    url = 'https://www.jin10.com/'
    getlist(url)