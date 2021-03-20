# -*-coding:  utf-8 -*-
# @Time    :  2021/2/25 23:11
# @Author  :  Cooper
# @FileName:  httpbin.py
# @Software:  PyCharm

import scrapy
from scrapy import cmdline
import re


class TencentSpider(scrapy.Spider):
    #爬虫名称必须唯一
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/get']

    def parse(self, response):
        '''
        用于提取数据或者提取新的URL
        :param response: 就是request对应的响应
        :yield: 返回item对象或者字典给引擎，引擎就把这个数据交给Pipline
        如果返回request对象，那么引擎就会把这个request对象交给调度器进行处理
        '''
        print('-'*25)
        print(response.text)
        print('-'*25)
        yield scrapy.Request('https://httpbin.org/get',dont_filter=True)

if __name__ == '__main__':
        cmdline.execute("scrapy crawl httpbin ".split())#)意味着根据任何空格分割