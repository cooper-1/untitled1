# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 16:32:22 2021

@author: kimol_love
"""
import os
import time
import requests
from bs4 import BeautifulSoup


def search_article(artName):
    '''
    搜索论文
    ---------------
    输入：论文名
    ---------------
    输出：搜索结果（如果没有返回""，否则返回PDF链接）
    '''
    url = 'https://www.sci-hub.ren/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/x-www-form-urlencoded',
               'Content-Length': '123',
               'Origin': 'https://www.sci-hub.ren',
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': '1'}
    data = {'sci-hub-plugin-check': '',
            'request': artName}
    res = requests.post(url, headers=headers, data=data)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    iframe = soup.find(id='pdf')
    if iframe == None:  # 未找到相应文章
        return ''
    else:
        downUrl = iframe['src']
        if 'http' not in downUrl:
            downUrl = 'https:' + downUrl
        return downUrl


def download_article(downUrl):
    '''
    根据论文链接下载文章
    ----------------------
    输入：论文链接
    ----------------------
    输出：PDF文件二进制
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
               'Accept-Encoding': 'gzip, deflate, br',
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': '1'}
    res = requests.get(downUrl, headers=headers)
    return res.content


def welcome():
    '''
    欢迎界面
    '''
    os.system('cls')
    title = '''
               _____  _____ _____      _    _ _    _ ____  
              / ____|/ ____|_   _|    | |  | | |  | |  _ \ 
             | (___ | |      | |______| |__| | |  | | |_) |
              \___ \| |      | |______|  __  | |  | |  _ < 
              ____) | |____ _| |_     | |  | | |__| | |_) |
             |_____/ \_____|_____|    |_|  |_|\____/|____/


            '''
    print(title)


if __name__ == '__main__':
    while True:
        welcome()
        request = input('请输入URL、PMID、DOI或者论文标题：')
        print('搜索中...')
        downUrl = search_article(request)
        if downUrl == '':
            print('未找到相关论文，请重新搜索！')
        else:
            print('论文链接：%s' % downUrl)
            print('下载中...')
            pdf = download_article(downUrl)
            with open('%s.pdf' % request, 'wb') as f:
                f.write(pdf)
            print('---下载完成---')
        time.sleep(0.8)
