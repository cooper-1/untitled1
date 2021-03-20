# -*-coding:  utf-8 -*-
# @Time    :  2020/12/18 16:01
# @Author  :  Cooper
# @FileName:  别人的爬虫.py
# @Software:  PyCharm
# encoding=utf-8
import bs4
from bs4 import BeautifulSoup
import requests
import os


def get_html(url):
    try:
        header = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"}
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()
        print(r.text)
        return r.text
    except:
        return "error"


def print_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    content_list = soup.find_all('div', attrs={'class': 'info'})
    # os.mkdir(path)

    print(type(content_list))
    print(len(content_list))

    for content in content_list:
        title = content.find('span').text
        star = content.find('p').text.replace('&nbsp', '').replace('    ', '')

        link = content.a['href']
        title = content.find('span').text
        print(link)
        print(title)
        html = get_html(link)
        if (html != "error"):
            soup = BeautifulSoup(html, 'lxml')
            summary = soup.find('span', {'property': 'v:summary'}).text.replace(' ','')
            # print(summary)
        else:
            print("None")

        fpath = path + "\\" + title + ".txt"
        with open(fpath, 'w', encoding="utf-8") as f:
            f.write(title)
            f.write(star)
            f.write(summary)
        f.close()


i = 0
while i < 250:
    path = "E:\\电影"
    url = "https://movie.douban.com/top250?start=" + str(i)
    html = get_html(url)
    print_content(html)
    i = i + 25