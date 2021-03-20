# -*-coding:  utf-8 -*-
# @Time    :  2020/12/17 20:43
# @Author  :  Cooper
# @FileName:  crawl4.py
# @Software:  PyCharm

import requests
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
a=0
class QuotesSpider(scrapy.Spider):
    name = "quotes4"
    def start_requests(self):
        urls=['https://quotes.toscrape.com/page/1/']#设置爬取目标的地址'https://quotes.toscrape.com/page/2/'
        #获取所有地址，有几个地址发送几次请求

        for url in urls:
            #发送网络请求
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        # 获取所有信息
        global a
        a = a + 1
        for quote in  response.xpath(".//*[@class='quote']"):
            # 获取名言
            text = quote.xpath(".//*[@class='text']/text()").extract_first()
            #获取作者
            author=quote.xpath(".//*[@class='author']/text()").extract_first()

            print(text)#输出作者
            print(author)#输出作者

            page=response.url.split("/")[-2]
            filename = 'quotes-%s.txt' % a

            with open(filename, 'a+', encoding='utf-8') as f:
                f.write(text +'———————————'+ author+'\n'+'\n')
            self.log('Saved file %s' % filename)


        #实现翻页
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href,self.parse)

if __name__=='__main__':
    #创建类对象并传入项目设置信息参数
    process=CrawlerProcess(get_project_settings())
    #设置需要启动的爬虫名称
    process.crawl('quotes4')
    #启动爬虫
    process.start()



