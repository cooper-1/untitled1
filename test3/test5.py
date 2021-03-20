# -*-coding:  utf-8 -*-
# @Time    :  2021/3/18 16:32
# @Author  :  Cooper
# @FileName:  test5.py
# @Software:  PyCharm
import requests
#实例化session
session = requests.session()

from requests.exceptions import ReadTimeout,HTTPError,RequestException
import re
import time
import random

j=0


headers={
'authority': 'uc-api.jin10.com',
'method': 'POST',
'path': '/login_w',
'scheme': 'https',
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'content-length': '90',
'content-type': 'application/json;charset=UTF-8',
'cookie': 'Hm_lvt_522b01156bb16b471a7e2e6422d272ba=1616054920; UM_distinctid=1784461251381-0a5f2ad4b2ff9b-376b4502-1fa400-17844612514334; login_redirect=; XSRF-TOKEN=eyJpdiI6IkdIeHIyU3p4bk1sOEhJVU5XR3M0QUE9PSIsInZhbHVlIjoiVTNEcitjQUMyZzFJcmNEZEUrRjJFQT09IiwibWFjIjoiYWNlYzg3OWVmYTM5OTNhYjM2NWRhMjg5ZjdiNzNkN2Y3MWEyNzYyYzM1YWZkZGQzZWIwZWQ3M2I2YWI0YTFhNSJ9; laravel_session=eyJpdiI6ImJMSm1xb21FYU9yVGgrakIxUzBsamc9PSIsInZhbHVlIjoiSElBeTkrNThRT1JWeXFPZVFUMk9qS0RFMzNMekdPbVJLUGFJUHA0bm1lWWU5bDF4ZFVaU1hvOVwvMWhTUmZGK3RzcThFdWJlbUhXM1RUYUxoVjZseUx3PT0iLCJtYWMiOiJkNGQ4OGViOGMxYTYyNDg0YWU3NmRlMTc2ZmI5MTljMGFkM2FhM2U1NjEzNWVkMmU3Zjg5MTJhODM5Yjg0ODQ0In0%3D; x-token=; Hm_lpvt_522b01156bb16b471a7e2e6422d272ba=1616068870',
'origin': 'https://www.jin10.com',
'referer': 'https://www.jin10.com/',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'x-app-id': 'YDcStOzjliuTJUvh',
'x-app-ver': 'web_base_1.0.0',
'x-version': '1.0.0',
'x-xsrf-token': 'eyJpdiI6IkdIeHIyU3p4bk1sOEhJVU5XR3M0QUE9PSIsInZhbHVlIjoiVTNEcitjQUMyZzFJcmNEZEUrRjJFQT09IiwibWFjIjoiYWNlYzg3OWVmYTM5OTNhYjM2NWRhMjg5ZjdiNzNkN2Y3MWEyNzYyYzM1YWZkZGQzZWIwZWQ3M2I2YWI0YTFhNSJ9',
}

postdata={'mobile': "18819776051",' password': "970999ef69b887266d4696570cee8bbc",
          'remenber':'forever',
          'testcookie':'1',
          'country_code': "CN",'referer': 'https://www.jin10.com/',}
url='https://uc-api.jin10.com/login_w'
login=session.post(url,data=postdata,headers=headers)
print(login.status_code)