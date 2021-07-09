# -*-coding:  UTF-8
# @Time    :  2021/5/28 22:56
# @Author  :  Cooper
# @FileName:  json模块的基本使用.py
# @Software:  PyCharm
import json

# loads 把json转换为python类型的对象
# json的字符串对象
json_obj = '{"name":"小米","age":"18","gender":"male"}'
dic = json.loads(json_obj)
print(dic)  # {'name': '小米', 'age': '18', 'gender': 'male'}
print(type(dic))  # <class 'dict'>

# dumps 把python类型的对象转换为json 默认使用ASCII进行编码
json_obj2 = json.dumps(dic)
print(json_obj2)  # {"name": "\u5c0f\u7c73", "age": "18", "gender": "male"}
print(type(json_obj2))  # <class 'str'>
# ensure_ascii 是否要使用ASCII进行编码默认True，如果禁用就是false那么就以按utf-8进行编码
json_obj3 = json.dumps(dic, ensure_ascii=False)
print(json_obj3)  # {"name": "小米", "age": "18", "gender": "male"}

# 把json进行格式化字符串,indent参数来指定。表示缩进的字符数。
json_obj4 = json.dumps(dic, ensure_ascii=False, indent=2)
print(json_obj4)

# 把json写入文件中
with open('person.json', 'w') as f:
    # json.dump(dic, f)  # {"name": "\u5c0f\u7c73", "age": "18", "gender": "male"}
    # f.write('\n')
    # json.dump(dic, f, ensure_ascii=False)  # {"name": "小米", "age": "18", "gender": "male"}
    # f.write('\n')
    json.dump(dic, f, ensure_ascii=False, indent=2)  # {"name": "小米", "age": "18", "gender": "male"}
# 把文件对象转化为json
with open('person.json', 'r') as f:
    dic2 = json.load(f)
    print(dic2)
