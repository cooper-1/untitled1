# -*-coding:  utf-8 -*-
# @Time    :  2021/1/24 20:00
# @Author  :  Cooper
# @FileName:  页面的前进和后退.py
# @Software:  PyCharm
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.get("http://news.baidu.com/")
#点击新闻
driver.find_element_by_link_text('图片').click()
time.sleep(1)
#页面后退
driver.back()
time.sleep(1)
#页面前进
driver.forward()
time.sleep(1)
driver.quit()