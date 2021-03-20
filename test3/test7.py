# -*-coding:  utf-8 -*-
# @Time    :  2021/3/18 18:12
# @Author  :  Cooper
# @FileName:  test7.py
# @Software:  PyCharm
import requests
import http.cookiejar as cookielib


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
}
url = 'https://uc-api.jin10.com/login_w'
seesion=requests.session()

seesion.cookies=cookielib.LWPCookieJar(filename='cookie')
try:
    seesion.cookies.load(ignore_discard=True)
except:
    print('错误')