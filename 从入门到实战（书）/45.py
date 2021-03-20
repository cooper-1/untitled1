# -*-coding:  utf-8 -*-
# @Time    :  2020/12/22 12:54
# @Author  :  Cooper
# @FileName:  45.py
# @Software:  PyCharm
from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path = r'C:\Users\86186\PycharmProjects\geckodriver.exe')
#把上述地址改成你电脑中geckodriver.exe程序的地址
driver.implicitly_wait(10) # 隐性等待，最长等20秒
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
time.sleep(5)
for page in range(1,22):
    print("第"+str(page)+"页")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-900);")
# 转换iframe，再找到查看更多，点击
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
    comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print(content.text)
#判断是否是整十的页数
if page%10 == 0:
    button = driver.find_element_by_css_selector('button.page-last-btn')
    button.click()
else :
    load_more = driver.find_element_by_xpath("//button[@data-page='" + str(page+1) + "']" )
    load_more.click()

# 把iframe又转回去
driver.switch_to.default_content()
time.sleep(2)