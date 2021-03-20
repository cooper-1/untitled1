# -*-coding:  utf-8 -*-
# @Time    :  2021/1/24 20:44
# @Author  :  Cooper
# @FileName:  页面等待.py
# @Software:  PyCharm

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions#条件模块
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id('kw').send_keys('进击的巨人')
driver.find_element_by_id('su').click()
#显示等待
# def __init__(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None):
#driver:浏览器驱动对象
#timeout 最长等待时间
#poll_frequency=每隔多久判断一下条件
#until 等待某个条件满足为止
#expected_conditions#提供了很多条件模块判断条件的方法
#presence_of_elements_located判断某个元素是否加载完成，这个方法中传入的元组
# element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'下一页 >')))
# # # print(element)
#隐式等待：指定最大等待时间
# driver.implicitly_wait(5)
time.sleep(5)
print('_'*50)
# 获取下一页的a标
#下一页<
nextpage=driver.find_element_by_link_text('下一页 >')
driver.find_element_by_link_text('下一页 >').click()
print(nextpage)
time.sleep(1)
driver.quit()