# -*-coding:  utf-8 -*-
# @Time    :  2021/2/22 22:01
# @Author  :  Cooper
# @FileName:  bilibili.py
# @Software:  PyCharm
import scrapy
from scrapy import cmdline
import re


class TencentSpider(scrapy.Spider):
    #爬虫名称必须唯一
    name = 'bi'
    allowed_domains = ['toscrape.com']
    start_urls = ['https://quotes.toscrape.com/page/1/']

    def parse(self, response):
        '''
        用于提取数据或者提取新的URL
        :param response: 就是request对应的响应
        :yield: 返回item对象或者字典给引擎，引擎就把这个数据交给Pipline
        如果返回request对象，那么引擎就会把这个request对象交给调度器进行处理
        '''
        item = {}
        pattern = re.compile('<span class="text" itemprop="text">(.*?)</span>', re.S)  # <img class="" src=
        texts = pattern.findall(response.text)
        print(texts)
        pattern = re.compile(' <span>by <small class="author" itemprop="author">(.*?)</small>', re.S)  # <img class="" src=
        authors = pattern.findall(response.text)
        print(authors)
        for  index,text in enumerate(texts):
            print(text)
            item['text'] = text
            print(authors[index])
            item['text'] = authors[index]
            # 如何把数据交给引擎，可以使用yield(英文产物产出的意思)关键字把数据交给引擎
            yield item
        #实现翻页效果
        pattern = re.compile('<li class="next">\s*<a href="(.*?)">',re.S)  # <img class="" src=
        nexturl=pattern.findall(response.text)
        print(nexturl)

        if nexturl !=[]:
            nexturl ='https://quotes.toscrape.com/'+ nexturl[0]
            print(nexturl,'-------------------------------')
            '''
            第一参数url
            callback：该请求对应的响应交给爬虫的那个解析方法进行处理
            dont_filter：如果为True，就是请求过了也会继续请求，如果为false，请求过了不会再请求
            '''

            yield scrapy.Request(nexturl,callback=self.parse,dont_filter=False)






if __name__ == '__main__':
        cmdline.execute("scrapy crawl bi ".split())#)意味着根据任何空格分割