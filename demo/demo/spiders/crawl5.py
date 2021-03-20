# -*-coding:  utf-8 -*-
# @Time    :  2020/12/17 21:50
# @Author  :  Cooper
# @FileName:  crawl5.py
# @Software:  PyCharm

import requests
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from untitled1.demo.demo.items import  DemoItem


class QuotesSpider(scrapy.Spider):
    name = "quotes5"
    def start_requests(self):
        urls=['https://quotes.toscrape.com/page/1/']#设置爬取目标的地址'https://quotes.toscrape.com/page/2/'
        #获取所有地址，有几个地址发送几次请求
        for url in urls:
            #发送网络请求
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        # 获取所有信息
        for quote in  response.xpath(".//*[@class='quote']"):
            # 获取名言
            text = quote.xpath(".//*[@class='text']/text()").extract_first()
            #获取作者
            author=quote.xpath(".//*[@class='author']/text()").extract_first()
            tags = quote.xpath(".//*[@class='tag']/text()").extract_first()
            item=DemoItem(text=text,author=author,tags=tags)
            yield item
            filename = 'quotes-0.txt'
            with open(filename, 'a+', encoding='utf-8') as f:
                f.write(str(item))
            self.log('Saved file %s' % filename)


if __name__=='__main__':
    #创建类对象并传入项目设置信息参数
    process=CrawlerProcess(get_project_settings())
    #设置需要启动的爬虫名称
    process.crawl('quotes5')
    #启动爬虫
    process.start()


