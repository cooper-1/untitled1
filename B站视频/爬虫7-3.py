# -*-coding:  utf-8 -*-
# @Time    :  2020/12/19 14:59
# @Author  :  Cooper
# @FileName:  爬虫7-3.py
# @Software:  PyCharm
import requests,re
import time
from requests.exceptions import ReadTimeout,HTTPError,RequestException
from bs4 import BeautifulSoup

url='https://www.baidu.com'

key_dict={'wd':'美女'}
headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
         'Host':'www.baidu.com'}
proxy={'http':'175.155.141.242 :1133'}
if __name__ == "__main__":
    time.sleep(2)

    response=requests.get(url,params=key_dict,headers=headers,proxies=proxy,timeout=30)
    print(' 页响应状态码：',response.status_code)
    #print(response.content.decode('utf-8'))
    page_text = response.text
    filename = 'quotes-%s.html' % 5
    with open(filename, 'a+', encoding='utf-8') as fp:
        fp.write(response.content.decode('utf-8'))
    print(filename, '保存成功！！！')
