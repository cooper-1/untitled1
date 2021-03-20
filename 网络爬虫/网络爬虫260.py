# -*-coding:  utf-8 -*-
# @Time    :  2020/12/16 14:27
# @Author  :  Cooper
# @FileName:  网络爬虫260.py
# @Software:  PyCharm
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException

url='https://www.baidu.com/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
#response=requests.get(url,headers=headers)
#循环发送请求50次
for a in range(1,50):
    try:#捕获异常
            #response=requests.get('https://www.whatismyip.com/',timeout=0.5)#设置超时时间
            response = requests.get(url, headers=headers,timeout=0.05)
            print(response.status_code)
    except ReadTimeout:
        print('超时异常')
    except HTTPError:
        print('HTTTp异常')
    except RequestException:
        print('请求异常')



