# -*-coding:  utf-8 -*-
# @Time    :  2020/12/16 14:12
# @Author  :  Cooper
# @FileName:  网络爬虫230.py
# @Software:  PyCharm
import requests
#循环发送请求50次
for a in range(1,50):
    try:#捕获异常
            response=requests.get('https://www.baidu.com/',timeout=0.05)#设置超时时间
            print(response.status_code)
    except Exception as e:
        print('异常'+str(e))