# -*-coding:  utf-8 -*-
# @Time    :  2021/3/3 15:40
# @Author  :  Cooper
# @FileName:  处理redis数据库中的数据.py
# @Software:  PyCharm
from pymongo import MongoClient
from redis import Redis
import json
#把redis数据库的爬虫数据到MongoDB数据库中，从而降低内存消耗
def redis_to_pymongo():
    #连接redis数据库
    redis_cli=Redis('121.37.162.236',6379)
    #连接MongoDB数据库
    mongo_cli=MongoClient('127.0.0.1',27017)
    #获取MongoDB数据库中用于储存数据的集合
    clo=mongo_cli['itcast']['item']
    #使用while死循环，不断读取redis数据库的内容，添加到MongoDB数据库中
    while True:
        #从redis数据库中取出内容
        #FIFO:blpop,FILO:brpop
        source,item=redis_cli.blpop('itcast:items')
        # 把item转化为字典数据
        data=json.loads(item)
        clo.insert_one(data)
        # clo.insert(data)
if __name__ == '__main__':
    redis_to_pymongo()