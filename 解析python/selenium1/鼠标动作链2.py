# -*-coding:  utf-8 -*-
# @Time    :  2021/1/22 23:34
# @Author  :  Cooper
# @FileName:  鼠标动作链2.py
# @Software:  PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://ssl.zc.qq.com/v3/index-chs.html?type=3")
driver.switch_to.frame(0)
#获取滑块元素
thumb=driver.find_element_by_id('tcaptcha_drag_thumb')
print(thumb)
#获取反馈元素# id="e_showFB"
fk=driver.find_element_by_id("e_showFB")
print(fk)
time.sleep(1)
# ActionChains(driver).drag_and_drop(thumb,fk).perform()
ActionChains(driver).drag_and_drop_by_offset(thumb,170,0).perform()

time.sleep(3)
driver.quit()
