# -*-coding:  utf-8 -*-
# @Time    :  2021/3/18 19:49
# @Author  :  Cooper
# @FileName:  test10.py
# @Software:  PyCharm
import requests

headers = {
    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
}

# 设置一个会话session对象s
s = requests.session()
resp = s.get('https://www.baidu.com/s?wd=python', headers=headers)
# 打印请求头和cookies
print(resp.request.headers)
print(resp.cookies)

# 利用s再访问一次
resp = s.get('https://www.baidu.com/s?wd=python', headers=headers)

# 请求头已保持首次请求后产生的cookie
print(resp.request.headers)
print(resp.cookies)