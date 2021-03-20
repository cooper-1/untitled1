# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class SpiderPipeline:
    def process_item(self, item, spider):
        '''
        必须实现
        用于处理item对象
        1.检查字段
        2.去重
        3.保存数据
        :param item: 爬虫提取的数据
        :param spider: 该数据对应的爬虫对象
        :return: 必须返回一个item对象，或字典，或none
        返回的数据会交给后面发item Pipeline进行处理
        如果处理完毕了，该item处理到此结束，可以抛出一个DropItem的异常
        每个item都会调用一次，调用频率很快
        如果在这个方法中打开文件和关闭文件就会非常消耗资源
        '''
        print(item)
        json.dump(item,self.file,ensure_ascii=False)
        self.file.write('\n')
        return item
    def open_spider(self,spider):
        '''
        当爬虫启动的时候执行
        :param spider: 开启的爬虫 对象
        '''
        print('open_spider')
        #打开文件对象
        self.file=open('hr.txt','a+',encoding='utf-8')
    def close_spider(self,spider):
        '''
        当爬虫关闭的时候执行
        :param spider: 开启的爬虫 对象
        '''
        print('close_spider')
        # 关闭文件对象
        self.file.close()