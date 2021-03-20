# -*-coding:  utf-8 -*-
# @Time    :  2021/1/23 22:12
# @Author  :  Cooper
# @FileName:  弹窗处理.py
# @Software:  PyCharm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
#弹窗
#准备弹窗的js
js="alert('你好')"
#执行js
driver.execute_script(js)
#关闭窗口

time.sleep(1)

#获取弹窗对象
alert=driver.switch_to_alert()#过时方式
print(alert.text)
alert=driver.switch_to.alert#推荐方式
print(alert.text)
alert.dismiss()
time.sleep(2)
driver.quit()