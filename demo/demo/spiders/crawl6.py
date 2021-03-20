# -*-coding:  utf-8 -*-
# @Time    :  2020/12/18 14:26
# @Author  :  Cooper
# @FileName:  crawl6.py
# @Software:  PyCharm

import requests
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from untitled1.demo.demo.items import  DemoItem


class QuotesSpider(scrapy.Spider):
    name = "quotes6"
    def start_requests(self):
        url='https://movie.douban.com/top250?start='#设置爬取目标的地址'https://quotes.toscrape.com/page/2/'
        #获取所有地址，有几个地址发送几次请求
        for i in range(0, 10):
            url = url + str(i * 25)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 获取所有信息
        for quote in response.xpath(".//*[@class='info']"):
            # 获取名言
            movie_name = quote.xpath(".//*[@class='other']/text()").extract_first()

            print(movie_name)  # 输出

            #page = response.url.split("/")[-2]
            filename = 'quotes-1.txt'
            with open(filename, 'a+', encoding='utf-8') as f:
                f.write(movie_name + '\n' + '\n')
            self.log('Saved file %s' % filename)


if __name__=='__main__':
    #创建类对象并传入项目设置信息参数
    process=CrawlerProcess(get_project_settings())
    #设置需要启动的爬虫名称
    process.crawl('quotes6')
    #启动爬虫
    process.start()


