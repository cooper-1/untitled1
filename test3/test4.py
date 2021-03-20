# -*-coding:  utf-8 -*-
# @Time    :  2021/3/18 16:11
# @Author  :  Cooper
# @FileName:  test4.py
# @Software:  PyCharm

from selenium import webdriver
import time
options = webdriver.ChromeOptions()
# options.headless=True  #设置选项为无界面
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(options=options)
driver.get("https://www.jin10.com/")
time.sleep(2)
suspondWindow = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/span/a[1]')#登录
suspondWindow.click()
time.sleep(1)
suspondWindow = driver.find_element_by_xpath('//*[@id="login_phone"]')#账号
suspondWindow.send_keys('18819776051')
time.sleep(1)
suspondWindow = driver.find_element_by_xpath('//*[@id="login_pwd"]')#密码
suspondWindow.send_keys('1274814498.qq')
time.sleep(1)
suspondWindow = driver.find_element_by_xpath('//*[@id="modal_login"]/div/div[2]/div[1]/form/button')#点登录
suspondWindow.click()
time.sleep(2)
co=driver.get_cookies()
driver.get_cookies().save()
# print(driver.page_source)
print(co)
driver.quit()
# for  a in co:
#     print(a)
# with open('cookie','w') as f:
#     for  a in co:
#         f.write(str(a))

# import requests
# import http.cookiejar as cookielib
#
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
# }
# url = 'https://uc-api.jin10.com/login_w'
# seesion=requests.session()
#
# seesion.cookies=cookielib.LWPCookieJar(filename='cookie')
# try:
#     seesion.cookies.load(ignore_discard=True)
# except:
#     print('错误')