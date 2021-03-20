# -*-coding:  utf-8 -*-
# @Time    :  2021/1/23 20:40
# @Author  :  Cooper
# @FileName:  填充表单.py
# @Software:  PyCharm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
driver.get("https://e.weibo.com/register/register")
#把driver切换到注册的iframe中
driver.switch_to.frame(0)
# 获取下拉选择框
province=driver.find_element_by_name('province')
# print(province)
#选择北京
Select(province).select_by_index(1)#根据索引进行选择
time.sleep(2)
Select(province).select_by_value('50')#根据索引进行选择
time.sleep(2)
Select(province).select_by_visible_text('广西')#根据索引进行选择
time.sleep(2)
#取消选择，在单选的select中不支持任何取消选择，只有多选才支持取消选择
driver.quit()