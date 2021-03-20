# -*-coding:  utf-8 -*-
# @Time    :  2020/12/18 20:35
# @Author  :  Cooper
# @FileName:  头条爬虫.py
# @Software:  PyCharm
import json
import re
import urllib.request
from urllib.parse import urlencode
import requests

url = "https://www.toutiao.com/search_content/?"
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}


def get_page_url(url, offset, keyword):
    parse = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from_': 'search_tab'
    }
    url = url + urlencode(parse)
    all_url = []
    try:
        req = requests.get(url=url, headers=headers)
        offset_dict = json.loads(req.text)
        for item in offset_dict['data']:  # 循环读取列表  相当于一个个详情快
            if 'has_gallery' in item:  # 是否有该属性
                if item['has_gallery'] == True:  # 是否为True属性 该属性是判断文章图片的展示方式
                    all_url.append(item['article_url'])  # 加入列表
                else:
                    pass
            else:
                pass
    except Exception as msg:
        print('Error' + msg)
    return all_url


def get_img_url(req):
    ajax_data = re.findall('gallery: JSON.parse(.*?)\n', req.text)
    data = ajax_data[0].replace('\\', '')
    data_json = re.findall('"url":"(.*?)"', data)  # data_json去要去重
    pic_url = []
    for i in range(0, len(data_json), 4):  # 每张图片有四个地址，选取其中一个就好了
        pic_url.append(data_json[i])
    for url in pic_url:
        try:
            urllib.request.urlretrieve(url=url, filename='E:/jr/%s.jpg' % url[-5:])  # 以图片地址的后五位字符命名
        except:
            pass


def parse_page(all_url):
    for url in all_url:
        req = requests.get(url=url, headers=headers)
        get_img_url(req)


if __name__ == '__main__':
    for i in range(0, 100, 20):
        all_url = get_page_url(url=url, offset=i, keyword='街拍')
        parse_page(all_url)