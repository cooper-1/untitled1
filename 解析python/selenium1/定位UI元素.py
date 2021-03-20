# -*-coding:  utf-8 -*-
# @Time    :  2021/1/22 20:42
# @Author  :  Cooper
# @FileName:  定位UI元素.py
# @Software:  PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


#创建option对象
option=Options()
#设置选项为无界面
option.headless=True
# 使用option配置chrome浏览器
driver=webdriver.Chrome(options=option)
driver.get("https://www.baidu.com/")
input=driver.find_element_by_id('kw')
print(input.get_attribute('class'))
input=driver.find_element(By.ID,'kw')
print(input.get_attribute('class'))
input=driver.find_element(By.NAME,'wd')
print(input.get_attribute('class'))
input=driver.find_element_by_name('wd')
print(input.get_attribute('class'))
hao123=driver.find_element_by_partial_link_text('hao')
print(hao123.get_attribute('href'))
hao123=driver.find_element_by_link_text('hao123')
print('---------------------------',hao123.get_attribute('href'))
input=driver.find_elements_by_tag_name('input')
for a in input:
    print(a.get_attribute('type'))
tieba=driver.find_element_by_css_selector('#s-top-left > a:nth-child(6)')
print(tieba.get_attribute('text'))
a_s=driver.find_elements_by_xpath('//*[@id="s-top-left"]/a')
for a in a_s:
    print(a.text)