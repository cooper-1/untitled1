# -*-coding:  UTF-8
# @Time    :  2021/5/29 23:24
# @Author  :  Cooper
# @FileName:  jsonpath语法.py
# @Software:  PyCharm
import jsonpath
import json

# 准备json字符串数据
json_str = '''
{
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}
'''
# 把json字符串转换为python对象
store = json.loads(json_str)
# 查看store下bicycle的color属性
jsonurl = '$.store.bicycle.color'
result = jsonpath.jsonpath(store, jsonurl)
print(result)
# 跨级查找
jsonurl = '$..color'
result = jsonpath.jsonpath(store, jsonurl)
print(result)
# 输出book列表中包含的所有对象
jsonurl = '$.store.book'  # 一样的结果
jsonurl = '$.store.book[*]'
result = jsonpath.jsonpath(store, jsonurl)
print(result)
# 输出book列表的第一个对象，索引是从零开始的
jsonurl = '$.store.book[0]'
result = jsonpath.jsonpath(store, jsonurl)
print(result)
# 输出book列表的所有对象对应的title属性
jsonurl = '$.store.book[?(@.category =="fiction")]'
result = jsonpath.jsonpath(store, jsonurl)
print(result)
# 输出book列表的所有对象price小于10的对象
jsonurl = '$.store.book[?(@.price<10)]'
result = jsonpath.jsonpath(store, jsonurl)
print(result)
# 输出book列表的所有对象含有isbn的对象
jsonurl = '$.store.book[?(@.isbn)]'
result = jsonpath.jsonpath(store, jsonurl)
print(result)