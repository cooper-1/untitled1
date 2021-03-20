# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class SpiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SpiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # 当引擎把请求交给下载器的时候，都会经过改方法
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:必须返回下面4种情况中的一个
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        #当下载器把响应交给引擎的时候，会经过该方法
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
'''
1.定义下载器中间类
2.实现process_request
 2.1准备Usert-Agent列表，通常这种使用频繁的都会放到setting.py中
 2.2随机从Usert-Agent列表取出一个Usert-Agent
 2.3把它赋值给requests.headers['Usert-Agent']
3.在setting.py中，启动下载器中间件
'''
import random
from spider.settings import user_agent_list
from spider.settings import proxylist
class RandomUserAgent:
    def process_request(self,request,spider):
        user_agent =random.choice(user_agent_list)
        #2.3把它赋值给requests.headers['Usert-Agent']
        request.headers['User-Agent']=user_agent
class RandomProxy:
    def process_request(self, request, spider):

        # 1.在setting.py中准备代理的列表
        # 2.随机从中选择一个
        # 3.给请求设置代理IP

        proxy =random.choice(proxylist)
        print(proxy)
        #2.3把它赋值给requests.headers['Usert-Agent']
        request.meta['proxy'] = proxy
        return None