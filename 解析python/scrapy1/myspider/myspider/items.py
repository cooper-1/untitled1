# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#定义数据模型，明确要抓取的数据
#好处：
#1.提高代码的可读性
#2.避免手误把key写错
class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()#老师的姓名
    title = scrapy.Field()#老师的等级
    describe = scrapy.Field()#老师的描述

    pass
