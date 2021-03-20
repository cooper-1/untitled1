# -*-coding:  utf-8 -*-
# @Time    :  2021/1/22 22:16
# @Author  :  Cooper
# @FileName:  鼠标动作链.py
# @Software:  PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
# xw=driver.find_element_by_link_text('hao123')
# ActionChains(driver).move_to_element(xw).click().perform()
# xw=driver.find_element_by_link_text('新闻')
# ActionChains(driver).click(xw).perform()
# time.sleep(2)
xw=driver.find_element_by_link_text('hao123')
# ActionChains(driver).move_to_element(xw).double_click(xw).perform()
# xw=driver.find_element_by_link_text('新闻')
#双击
# ActionChains(driver).double_click(xw).perform()
#左键单击并且保持
# ActionChains(driver).click_and_hold(xw).perform()
#右击
ActionChains(driver).context_click(xw).perform()
time.sleep(2)

driver.quit()