# -*-coding:  utf-8 -*-
# @Time    :  2021/1/21 19:19
# @Author  :  Cooper
# @FileName:  sele.py
# @Software:  PyCharm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# driver=webdriver.PhantomJS()

#创建option对象
option=Options()
#设置选项为无界面
option.headless=True
# 使用option配置chrome浏览器
driver=webdriver.Chrome(options=option)
driver.get("https://www.baidu.com/")
#获取Id标签文本的内容
result=driver.find_element_by_id("s-top-left").text
print(result)

# #保存快照
# driver.save_screenshot('baidu.png')

#向搜索框中输入内容
driver.find_element_by_id('kw').send_keys("特朗普")

# 点击搜索按钮
driver.find_element_by_id('su').click()
time.sleep(2)

#通过模拟Ctrl+A
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
#通过模拟Ctrl+X
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
#在输入框重新输入搜索关键字
driver.find_element_by_id('kw').send_keys("拜登")
# 点击搜索按钮
driver.find_element_by_id('su').click()
time.sleep(2)
#清除搜索框
driver.find_element_by_id('kw').clear()
#获取当前页面的Cookie
print(driver.get_cookies())
#获取当前的URL
print(driver.current_url)

#获取title
print(driver.title)
time.sleep(2)
#获取页面源码
print(driver.page_source)
#关闭页面
driver.close()
time.sleep(1)
#退出驱动
driver.quit()