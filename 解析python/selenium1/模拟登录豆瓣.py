# -*-coding:  utf-8 -*-
# @Time    :  2021/1/24 22:51
# @Author  :  Cooper
# @FileName:  模拟登录豆瓣.py
# @Software:  PyCharm

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions#条件模块
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.douban.com/")
#把driver切换到注册的iframe中
driver.switch_to.frame(0)
time.sleep(2)
driver.find_element_by_class_name('account-tab-account').click()
#输入用户名
driver.find_element_by_class_name('account-form-input').send_keys('18819776051')
driver.find_element_by_id('password').send_keys('1274814498')
time.sleep(2)
driver.find_element_by_link_text('登录豆瓣').click()
time.sleep(2)
driver.quit()