import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import cmdline

#1.继承CrawlSpider
class Tencent1Spider(CrawlSpider):
    name = 'Tencent1'
    # allowed_domains = ['52dmtp.com']
    # start_urls = ['https://m.52dmtp.com/']
    allowed_domains = ['bilibili.com']
    start_urls = ['https://search.bilibili.com/article?keyword=p%E7%AB%99']
#rules用于定义从响应中提取URl的规则
    rules = (
        #LinkExtractor链接提取器,会自动的对url进行补全
        #allow 用于指定过滤链接正则表达式,如果为空就会提取所有的url,
        Rule(LinkExtractor(allow=r'https://www.bilibili.com/read/cv\d+\?from=search'), callback='parse_item',
             cb_kwargs={'name':'itcast'},
             process_links='process_links',
             follow=False,
             process_request=''),

    )

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
        cmdline.execute("scrapy crawl Tencent1 --nolog  ".split())  # )意味着根据任何空格分割
