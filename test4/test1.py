# -*-coding:  utf-8 -*-
# @Time    :  2021/3/19 12:49
# @Author  :  Cooper
# @FileName:  test1.py
# @Software:  PyCharm

from selenium import webdriver
import time,re
options = webdriver.ChromeOptions()
options.headless=True  #设置选项为无界面
# options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19')
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36')
driver = webdriver.Chrome(options=options)
# 确定目标的url
driver.get('https://bot.sannysoft.com/')
# 设置等待时间   等待服务器响应
driver.implicitly_wait(5)
# 窗口最大化
driver.maximize_window()
time.sleep(5)
print(driver.page_source)
driver.save_screenshot('安保.jpg')
driver.quit()