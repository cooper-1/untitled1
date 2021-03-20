# -*-coding:  utf-8 -*-
# @Time    :  2020/12/22 18:10
# @Author  :  Cooper
# @FileName:  10.py
# @Software:  PyCharm

import requests,re,json,_json
import time
from requests.exceptions import ReadTimeout,HTTPError,RequestException
from bs4 import BeautifulSoup

url='https://movie.douban.com/j/chart/top_list'

key_dict={'kw':'dog'}
param={'type': '24',
'interval_id': '100:90',
'action': '',
'start': '1',
'limit': '20'}
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
         }
proxy={'http':'175.155.141.242 :1133'}

if __name__ == "__main__":
    time.sleep(2)
    response=requests.get(url,params=param,headers=headers,proxies=proxy,timeout=30)
    print(' 页响应状态码：',response.status_code)
    print(response.content.decode('utf-8'))
    data_obj = response.json()
    filename = 'quotes-%s.txt' % 7
    fp = open(filename, 'a+', encoding='utf-8')
    json.dump(data_obj,fp=fp,ensure_ascii=False)
    print(filename, '保存成功！！！')