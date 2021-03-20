# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
import csv

class ItcastCSVPipeline:
    def open_spider(self,spider):
        '''
        当爬虫启动的时候执行，只会执行一次
        :param spider: 开启的爬虫 对象
        '''
        print('open_spider')
        #打开文件对象
        self.file=open('teacher.csv','wb')
        # self.f=open('itcast.csv','w',encoding='utf-8',newline='')
        #创建CSV格式数据的导出对象
        self.csv_exporter=CsvItemExporter(self.file)
        #启动数据导出
        self.csv_exporter.start_exporting()
        # self.csv_writer= csv.writer(self.f)

    def process_item(self, item, spider):
        '''
        每次引擎把数据交给pipeline的时候都会执行
        :param item:数据
        :param spider:爬虫
        :return:如果返回item，那么后面的pipeline可以对item进行处理，如果没有返回数据，那么后面的pipeline就没有办法对item进行处理了
        '''
        #把item数据以CSV格式数据写入文件中
        print(item)
        self.csv_exporter.export_item(item)
        # self.csv_writer.writerow(['dasd','describe', '架构师课程', 'name', '王老师', 'title','新东方'])
        print('ok')
        return item

    def close_spider(self,spider):
        '''
        当爬虫关闭的时候执行，用于释放资源
        :param spider: 开启的爬虫 对象
        '''
        print('close_spider')
        # 结束导出
        self.csv_exporter.finish_exporting()
        # 关闭文件对象
        self.file.close()
        # self.f.close()

from redis import Redis
import json
#写入到redis数据库
class ItcastRedisPipeline:
    def open_spider(self,spider):
        print('open_spider2')
        #连接redis数据库
        self.redis=Redis('121.37.162.236',6379)


    def process_item(self, item, spider):
        '''
        每次引擎把数据交给pipeline的时候都会执行
        :param item:数据
        :param spider:爬虫
        :return:如果返回item，那么后面的pipeline可以对item进行处理，如果没有返回数据，那么后面的pipeline就没有办法对item进行处理了
        '''
        #把item数据以字符串格式数据写入文件中
        json_str=json.dumps(dict(item),ensure_ascii=False)
        self.redis.lpush('itcast:teacher',json_str )
        return item


#写入到MongoDB数据库
from pymongo import MongoClient
class ItcastMongoDBPipeline:
    def open_spider(self,spider):
        print('open_spider3')
        #连接mongoDB数据库
        client=MongoClient('127.0.0.1',27017)
        #获取存取数据的集合
        self.clo=client['itcast']['teacher']



    def process_item(self, item, spider):
        '''
        每次引擎把数据交给pipeline的时候都会执行
        :param item:数据
        :param spider:爬虫
        :return:如果返回item，那么后面的pipeline可以对item进行处理，如果没有返回数据，那么后面的pipeline就没有办法对item进行处理了
        '''
        #插入数据
        self.clo.insert(dict(item))
        return item

