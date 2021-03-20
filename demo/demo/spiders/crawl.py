# -*-coding:  utf-8 -*-
# @Time    :  2020/12/16 18:46
# @Author  :  Cooper
# @FileName:  crawl.py
# @Software:  PyCharm
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls=['https://www.baidu.com/']#设置爬取目标的地址'https://quotes.toscrape.com/page/2/'
        #获取所有地址，有几个地址发送几次请求
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
        proxy = {'http': '175.42.68.184 :9999'}

        for url in urls:
            #发送网络请求
            yield scrapy.Request(url=url,dont_filter=True, callback=self.parse)
    def parse(self, response):
        #获取页数
        page=response.url.split
        #根据页面数量设置文件名称
        filename='quotes-6.html'
        #以只写方式的模式打开文件。如果没有改文件，则创建改文件
        with open(filename,'a+',encoding='utf-8') as f :
            f.write(response.body)
        self.log('Saved file %s'%filename)







        #导入CrawlerProcess类
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__=='__main__':
    #创建类对象并传入项目设置信息参数
    process=CrawlerProcess(get_project_settings())
    #设置需要启动的爬虫名称
    process.crawl('quotes')
    #启动爬虫
    process.start()



