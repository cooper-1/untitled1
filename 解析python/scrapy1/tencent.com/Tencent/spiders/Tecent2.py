# -*-coding:  utf-8 -*-
# @Time    :  2021/3/1 23:14
# @Author  :  Cooper
# @FileName:  Tecent2.py
# @Software:  PyCharm
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import cmdline

#1.继承CrawlSpider
class Tencent1Spider(CrawlSpider):
    name = 'Tencent2'
    # allowed_domains = ['52dmtp.com']
    # start_urls = ['https://m.52dmtp.com/']
    allowed_domains = ['bilibili.com']
    start_urls = ['https://search.bilibili.com/article?keyword=p%E7%AB%99']
    #rules用于定义从响应中提取URl的规则
    rules = (
        #LinkExtractor链接提取器,会自动的对url进行补全
        #allow 用于指定过滤链接正则表达式,如果为空就会提取所有的url,
        Rule(LinkExtractor(
            # allow=r'https://www.bilibili.com/read/cv\d+\?from=search',
            # deny=r'https://www.bilibili.com/read/cv\d+\?from=search',
            # restrict_xpaths=('//*[@id="article-list"]'),
            # tags=('script', ),
            # attrs=('src',),
            restrict_css=('#article-list'),
        ), callback='parse_item',
             process_links='process_links',
             follow=False,
            ),

    )
    '''def __init__(
        self,
        #用于指定提取链接的正则表达式
        allow=(),
        #用于指定不需要提取链接的正则表达式，优先级高于allow
        deny=(),
        #允许提取的域名
        allow_domains=(),
        #不允许提取的域名，优先级高于allow_domains
        deny_domains=(),
        #用于指定哪一个代码段的链接是需要提取的，如果没有指定则提取整个网页
        restrict_xpaths=(),
        # 需要提取哪些标签上的链接默认'a', 'area'
        tags=('a', 'area'),
        # 需要提取在标签上的属性，默认href属性
        attrs=('href',),
        # 是否要规范化url，默认是false
        canonicalize=False,
        # 相同的链接是否只提取一次，默认是true.3
        unique=True,
        # 用于指定一个函数，处理提取到的链接，可以更新链接，如果返回none表示这个链接被丢弃了，如果没有指定那么他就是lambda x:x
        process_value=None,
        #链接中不允许的后缀名比如.jpg
        deny_extensions=None,
        #使用css的语法指定哪些区域可以提取链接
        restrict_css=(),
        #提取到的链接是否需要去除俩端空格，默认是true
        strip=True,
        restrict_text=None,'''

    def process_links(self,links):
        '''
        过滤url
        :param links: link对象列表，link是对url的封装
        :return: 返回link列表
        '''
        for link in links:
            print('process_links=========%s'%link)
        return links

    def process_request(self,request):

        '''
        用于对request进行处理和过滤
        :param request: 如果返回request就会交给引擎进行处理，如果没有返回就会丢弃该请求
        :return:
        '''
        print('dfhsghshdgjfgsdjgfjsflsgfbcbjgsfey')
        #print('process_request:--------------------%s'%request)
        return request
#解析提取从Rule中提取URl所对应的响应
    def parse_item(self, response,**kwargs):
        print(response.url)
        print(kwargs)
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    if __name__ == '__main__':
        cmdline.execute("scrapy crawl Tencent2 --nolog  ".split())  # )意味着根据任何空格分割
