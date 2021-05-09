# -*-coding:  utf-8 -*-
# @Time    :  2021/3/18 15:50
# @Author  :  Cooper
# @FileName:  test3.py
from selenium import webdriver
import time, re
import csv
def get(url):
    options = webdriver.ChromeOptions()
    options.headless = True  # 设置选项为无界面
    options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    pattern = re.compile(r'<div class="presentation-item">(.*?)<div class="presentation-item">', re.S)
    result = pattern.findall(driver.page_source)
    print(len(result))
    with open(r"text2.csv", 'a+', encoding='UTF-8-sig', newline='') as f:
        for i in result:
            pattern = re.compile(r'[\u4e00-\u9fa5]+', re.S)
            work = pattern.findall(i)
            print(work)

            w = csv.writer(f)
            w.writerow(work)  # 注意这里
    driver.quit()
if __name__ == '__main__':
    urls = ["https://xiaoyuan.zhaopin.com/search/jn=2&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&pg={}".format(x) for x in range(1, 35)]
    for url in urls:
        get(url)