# -*-coding:  utf-8 -*-
# @Time    :  2021/2/18 22:52
# @Author  :  Cooper
# @FileName:  基本操作.py
# @Software:  PyCharm
from pymongo import *
#建立和mongoDB服务器的连接
# client = MongoClient('127.0.0.1',27017)#标准格式
#如果要连接的是默认端口的本地MongoDB连接，那么IP和端口号都是可以省略的
client= MongoClient()
print(client)
#获取数据库对象（如果有数据库对象就获取，没有就自动创建）
# 方式1：通过.的方式：来获取
# db=client.itcast

# 方式2：通过[]的方式：来获取
db=client['stu']
col=db.stu
print(col)
print(type(col))
#添加一条数据
col.insert({'name':'run', 'age':19})
col.insert_one({'name':'run', 'age':19})
#插入多条数据
# col.insert_many ([
#     {"_id":1,'name':'杨幂','age':35},
#     {"_id":2,'name':'asgf','age':45},
#     {"_id":3,'name':'翻山倒海监控','age':3},
#     {"_id":4,'name':'师傅说的话','age':355},
# ])
#查询一条数据
s=col.find_one()
# print(s)
#查询多条数据，返回的是一个游标对象，游标就可以进行遍历
cursor=col.find()
# print(cursor)
for data in cursor:
    print(data)
#根据条件进行查询，返回的是一个游标对象，游标就可以进行遍历
cursor=col.find({"age":19})
# print(cursor)
for data in cursor:
    print(data)

#更改一条数据
col.update_one({"name":'run'},{'$set':{'name':'jiang'}})
#更改多条数据
col.update_many({"age":20},{'$set':{'age':35}})
#删除一条数据
col.delete_one({"age":5})
#删除多条数据
col.delete_many({"age":19})
#查询多条数据，返回的是一个游标对象，游标就可以进行遍历
cursor=col.find()
# print(cursor)
for data in cursor:
    print(data)