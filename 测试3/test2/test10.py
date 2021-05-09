# -*-coding:  utf-8 -*-
# @Time    :  2021/3/12 19:24
# @Author  :  Cooper
# @FileName:  test10.py
# @Software:  PyCharm
# coding=utf-8
import json
from selenium import webdriver
import requests
import time


class cookies:
    def __init__(self, driver):
        self.driver = driver

    # 获取cookies保存到文件
    def save_cookie(self):
        cookies = self.driver.get_cookies()
        json_cookies = json.dumps(cookies)
        with open('cookies_csnd.json', 'w') as f:
            f.write(json_cookies)

    # 读取文件中的cookie
    def add_cookie(self):
        self.driver.delete_all_cookies()
        dict_cookies = {}
        with open('cookies.json', 'r', encoding='utf-8') as f:
            list_cookies = json.loads(f.read())
        for i in list_cookies:
            self.driver.add_cookie(i)


if __name__ == '__main__':
    url = 'https://live.kuaishou.com/u/kuaishouwzry?fid=593572317&cc=share_qqms&followRefer=151&shareMethod=MINI_PROGRAM&docId=5&kpn=KUAISHOU&subBiz=LIVE_STREAM&shareId=5963883811935&shareToken=Xvco16FUPqqZxj_A&shareResourceType=LIVESTREAM_OTHER&userId=701490839&shareType=5&et=1_a%2F0_unknown0&shareMode=APP&originShareId=5963883811935&appType=21&shareObjectId=Eh3FApfRCDQ&shareUrlOpened=0&timestamp=1615546778538'
    #cookie_list=[{"domain": "live.kuaishou.com", "expiry": 1615635784, "httpOnly": true, "name": "kuaishou.live.web_ph", "path": "/", "secure": false, "value": "f4ee24f0635982785ce3d89302671f44b66f"}, {"domain": "live.kuaishou.com", "expiry": 1615635784, "httpOnly": 'true', "name": "kuaishou.live.web_st", "path": "/", "secure": 'false', "value": "ChRrdWFpc2hvdS5saXZlLndlYi5zdBKgAYiNa2Aa6J5kzyQ5whciEowPSmF91KgAJaozF4pc02pDv8D51yRVhMOsTBA3iLfWktdvP5-d6hwkcJeYGQAySfUANzlCL0rSxLMq38QmsoGJhJ8tQDKS9ZRxsta8f5XmjALLzcFOhVFRm-CryMemaLBw39qrVCyZDY-yUo847nnmLNiXC4l36uFmwUe_rjqhZD1VMwLZ7hDAkBoHqyKzwxcaEiTUdhIhLkqeuKi4MmqrjKj9xSIgetMMjPOYNIF9OKaqS_-_7GHJgc71ZJLGD7aFSA-DkksoBTAB"}, {"domain": ".kuaishou.com", "expiry": 1617363785, "httpOnly": 'false', "name": "userId", "path": "/", "sameSite": "None", "secure": true, "value": "593572317"}, {"domain": "live.kuaishou.com", "expiry": 1615635784, "httpOnly": 'true', "name": "userId", "path": "/", "secure": false, "value": "593572317"}, {"domain": ".kuaishou.com", "expiry": 1647085383, "httpOnly": true, "name": "clientid", "path": "/", "secure": false, "value": "3"}, {"domain": "live.kuaishou.com", "expiry": 1647085383, "httpOnly": true, "name": "kpn", "path": "/", "secure": false, "value": "GAME_ZONE"}, {"domain": ".kuaishou.com", "expiry": 1647085383, "httpOnly": true, "name": "client_key", "path": "/", "secure": false, "value": "65890b29"}, {"domain": ".kuaishou.com", "expiry": 1647085383, "httpOnly": false, "name": "did", "path": "/", "secure": false, "value": "web_7a768be64da5780565317f48b07650ed"}, {"domain": "live.kuaishou.com", "httpOnly": true, "name": "kuaishou.live.bfb1s", "path": "/", "secure": false, "value": "477cb0011daca84b36b3a4676857e5a1"}]
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(5)
    driver.delete_all_cookies()
    with open(r'cookies_csnd.json', 'r', encoding='utf-8') as f:
        list_cookies = json.loads(f.read())
    for i in list_cookies:
        driver.add_cookie(i)
    driver.refresh()
    # # cookies.save_cookie()  # 保存cookies
    # driver.delete_all_cookies()  # 删除当前所有的cookies
    # # 打开想要跳转的界面，此步不可缺少，不然会报错
    # # driver.get(url)
    # cookies.add_cookies()  # 添加cookie
    # driver.get(url)  # 重新打开，该界面显示登录状