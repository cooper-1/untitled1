# -*-coding:  UTF-8
# @Time    :  2021/5/9 18:19
# @Author  :  Cooper
# @FileName:  lxml.py
# @Software:  PyCharm
# 导入etree模块
from lxml import etree
# Elment简介
# 1.创建节点（element对象）
root = etree.Element('root')
# 打印标签名
print(root.tag)
# 把Element对象转换为字符串
print(etree.tostring(root))
# 2.给节点添加属性
root = etree.Element('root',name='itcast')
# 打印标签名
print(root.tag)
# 把Element对象转换为字符串
print(etree.tostring(root))
# 2.2使用Element对象中set方法增加属性
root.set('age','15')
print(etree.tostring(root))
# 3.增加文本
root.text='hello, world!'
print(etree.tostring(root))
# 4.获取标签文本
print(root.text)
# 从字符串或文件中解析xml
# 准备xml字符串数据
xml_data='<root><a class="itcast"> data </a></root>'

# fromstring()函数：从字符串中解析XML文档或片段，返回根节点（或解析器目标返回的结果）。
element=etree.fromstring(xml_data)
print(element.tag)
print(etree.tostring(element))
#  XML()函数：从字符串常量中解析XML文档或片段，返回根节点（或解析器目标返回的结果）。
element=etree.XML(xml_data)
print(element.tag)
print(etree.tostring(element))
#  HTML()函数：从字符串常量中解析HTML文档或片段，返回根节点（或解析器目标返回的结果）。
# 有自动修正的HTML数据的功能
element=etree.HTML(xml_data)
print(element.tag)
print(etree.tostring(element))
# 查找与搜索元素
root = etree.XML("<root><a x='123'>aText<b/><c/><b/></a></root>")
print(root.xpath('//a')[0].tag)
# find()方法：返回匹配到的第一个子元素；
print(root.find('a').tag)
# findall()方法：以列表的形式返回所有匹配的子元素。
print(root.findall('a')[0].tag)
print(root.findall(".//a[@x]")[0].tag)

# iterfind()方法：返回一个所有匹配元素的迭代器。

