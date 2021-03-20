# -*-coding:  utf-8 -*-
# @Time    :  2020/12/16 20:06
# @Author  :  Cooper
# @FileName:  crawl2.py
# @Software:  PyCharm
import requests
import scrapy
from scrapy.crawler import CrawlerProcess    #导入CrawlerProcess类
from scrapy.utils.project import get_project_settings


class QuotesSpider(scrapy.Spider):
    name = "quotes1"
    def start_requests(self):
        urls=['https://quotes.toscrape.com/page/1/']#设置爬取目标的地址'https://quotes.toscrape.com/page/2/'

        #获取所有地址，有几个地址发送几次请求
        for url in urls:
            #发送网络请求
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        # 获取所有信息
        for quote in  response.xpath(".//*[@class='quote']"):
            text=quote.xpath(".//*[@class='text']/text()").extract_first()
            author=quote.xpath(".//*[@class='author']/text()").extract_first()
            tags=quote.xpath(".//*[@class='tag']/text()").extract_first()
            print(dict(text=text,author=author,tags=tags))
            filename = 'quotes-7.txt'
            with open(filename, 'a+', encoding='utf-8') as f:
                f.write(author+'\n')
            self.log('Saved file %s' % filename)

            # 实现翻页
        for href in response.css('li.next a::attr(href)'):
             yield response.follow(href, self.parse)

        #获取页数
        # page=response.url.split
        # #根据页面数量设置文件名称
        # filename='quotes-6.text'
        # #以写入方式的模式打开文件。如果没有改文件，则创建改文件
        # with open(filename,'wb') as f :
        #     f.write(response.body)
        # self.log('Saved file %s'%filename)

if __name__=='__main__':
    #创建类对象并传入项目设置信息参数
    process=CrawlerProcess(get_project_settings())
    #设置需要启动的爬虫名称
    process.crawl('quotes1')
    #启动爬虫
    process.start()



