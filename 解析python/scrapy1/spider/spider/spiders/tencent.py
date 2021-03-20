import scrapy
from scrapy import cmdline
import re


class TencentSpider(scrapy.Spider):
    #爬虫名称必须唯一
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1613921061791&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=1&pageSize=100&language=zh-cn&area=cn']

    def parse(self, response):
        '''
        用于提取数据或者提取新的URL
        :param response: 就是request对应的响应
        :yield: 返回item对象或者字典给引擎，引擎就把这个数据交给Pipline
        如果返回request对象，那么引擎就会把这个request对象交给调度器进行处理

        '''
        pattern = re.compile('{"Id"(.*?)},', re.S)  # <img class="" src=
        result = pattern.findall(response.text)
        # print(result)
        for data in result:
            item = {}
            # 职位名称
            pattern = re.compile('"RecruitPostName":"(.*?)"', re.S)  # <img class="" src=
            title = pattern.findall(data)[0]
            # print(title)
            item['title'] = title
            pattern = re.compile('"LocationName":"(.*?)",', re.S)  # <img class="" src=
            location = pattern.findall(data)[0]
            # print(name)
            item['location'] = location
            # pattern = re.compile('<h3>.*<span>(.*?)</span>.*</h3>', re.S)  # <img class="" src=

            pattern = re.compile('"Responsibility":"(.*?)",', re.S)  # <img class="" src=
            describe = pattern.findall(data)[0]
            # print(describe)
            item['describe'] = describe
            # print(item)

            # 如何把数据交给引擎，可以使用yield(英文产物产出的意思)关键字把数据交给引擎
            yield item

if __name__ == '__main__':
        cmdline.execute("scrapy crawl tencent  ".split())#)意味着根据任何空格分割