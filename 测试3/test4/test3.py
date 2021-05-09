# -*-coding:  utf-8 -*-
# @Time    :  2021/3/19 14:51
# @Author  :  Cooper
# @FileName:  test3.py
# @Software:  PyCharm
# 创建chrome参数对象
from selenium import webdriver
import time,re
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
options.add_argument('window-size=1600x900')  # 指定浏览器分辨率
options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36')
driver = webdriver.Chrome(options=options)
# 确定目标的url
# driver.get('https://supl.biz/proposals/search/?query=%D0%9C%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0')
driver.get('https://supl.biz/en/nasosnoe-oborudovanie-category477/')
driver.implicitly_wait(5)
# 窗口最大化
driver.maximize_window()
time.sleep(5)
print(driver.page_source)
driver.save_screenshot('安保2.png')
driver.quit()