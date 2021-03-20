import scrapy
import re
from scrapy_redis.spiders import RedisSpider
from Itcast.items import ItcastItem
from scrapy import cmdline


class ItcastSpider(RedisSpider):
    name = 'itcast'
    #允许的域名。可以写死，也可以动态生成
    allowed_domains = ['itcast.cn']
    # start_urls = ['http://itcast.cn/']
    #通过redis_redis来指定起始的url列表在redis数据库中的key
    #命名规范 爬虫名:start_url
    redis_key='itcast:start_url'
    def parse(self, response):
        '''
                当下载器把URL对应的响应交给引擎后，引擎就会调用爬虫的该方法
                用于处理响应的：解析提取的数据2。提取新的URL
                :param response: URL对应的响应数据
                '''
        # response.body:响应内容的二进数据
        # with open('teacher.html','wb') as f:
        #         #     f.write(response.body)
        pattern = re.compile('<div class="main_bot">(.*?)</div>', re.S)  # <img class="" src=
        divs = pattern.findall(response.text)
        print(len(divs))
        print(divs)
        for div in divs:
            # print(div)
            item = ItcastItem()
            pattern = re.compile('<h2>(.*?)<span>', re.S)  # <img class="" src=
            name = pattern.findall(div)[0]
            # print(name)
            item['name'] = name
            # pattern = re.compile('<h3>.*<span>(.*?)</span>.*</h3>', re.S)  # <img class="" src=
            pattern = re.compile('<h3>\s*<span>(.*?)</span>', re.S)  # <img class="" src=
            title = pattern.findall(div)[0]
            # print(title)
            item['title'] = title
            pattern = re.compile('<p>研发成果：\s*<span>(.*?)</span>', re.S)  # <img class="" src=
            describe = pattern.findall(div)[0]
            # print(describe)
            item['describe'] = describe
            # print(item)
            # 如何把数据交给引擎，可以使用yield(英文产物产出的意思)关键字把数据交给引擎
            yield item

if __name__ == '__main__':
    # 创建类对象
    # process=CrawlerProcess(get_project_settings())
    # #设置需要启动的爬虫名称
    # process.crawl('itcast')
    # process.start()#启动爬虫
    cmdline.execute("scrapy crawl itcast ".split())  # )意味着根据任何空格分割

