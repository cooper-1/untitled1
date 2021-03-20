# -*-coding:  utf-8 -*-
# @Time    :  2021/1/24 19:40
# @Author  :  Cooper
# @FileName:  页面切换.py
# @Software:  PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
#点击新鲜事
driver.find_element_by_id('lg').click()
for win in driver.window_handles:
    print(win)
    print(type(win))
time.sleep(2)
# 切换百度首页
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.quit()