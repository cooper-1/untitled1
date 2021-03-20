# -*-coding:  utf-8 -*-
# @Time    :  2021/1/24 20:09
# @Author  :  Cooper
# @FileName:  获取页面的cookie信息.py
# @Software:  PyCharm

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
#获取所有的cookie信息
print(driver.get_cookies())

for cookie in driver.get_cookies():
    print("%s=%s"%(cookie['name'],cookie['value']))
print('_'*20)
#根据名称删除cookie
driver.delete_cookie('H_PS_PSSID')
for cookie in driver.get_cookies():
    print("%s=%s"%(cookie['name'],cookie['value']))
print('_'*20)
#删除所有cookie
driver.delete_all_cookies()
time.sleep(1)
driver.quit()