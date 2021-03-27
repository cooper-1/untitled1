# -*-coding:  utf-8 -*-
# @Time    :  2021/3/18 15:50
# @Author  :  Cooper
# @FileName:  test3.py
# @Software:  PyCharm
# -*-coding:  utf-8 -*-
# @Time    :  2021/3/17 18:06
# @Author  :  Cooper
# @FileName:  test.py
# @Software:  PyCharm

# -*-coding:  utf-8 -*-
# @Time    :  2021/3/10 21:24
# @Author  :  Cooper
# @FileName:  爬取百度文库3.py
# @Software:  PyCharm
from selenium import webdriver
import time, re
def get(url):
    options = webdriver.ChromeOptions()
    # options.headless=True  #设置选项为无界面
    options.add_argument(
        'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    print(driver.page_source)  # 打印页面源码
    # driver.quit()
if __name__ == '__main__':
    urls=["https://xiaoyuan.zhaopin.com/search/jn=2&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&pg={}".format(x) for x in range(1,35)]
    for url in urls[:2]:
        get(url)