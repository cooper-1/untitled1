# -*-coding:  UTF-8
# @Time    :  2021/5/9 23:16
# @Author  :  Cooper
# @FileName:  lxml库的基本使用.py
# @Software:  PyCharm
# 导入lxml模块中的etree模块
from lxml import  etree
# 解析hello.html文件
# element与ElemenTree方法基本一致
element=etree.parse('hello.html')
print(element)
print(type(element))
# 通过element对象上的xpath方法来获取我们需要的对象
# 1.获取所有的li标签
# 如果xpath语法定位的是元素，则返回的是一个Element对象的列表
lis=element.xpath('//li')
print(lis )
print(type(lis))
for li in lis:
    print(li.tag)
# 2.获取所有的li标签的class属性：//li/@class
# 如果xpath语法定位的是属性或文本，则返回的是一个字符串的列表
liss=element.xpath('//li/@class')
print(liss)
# 3.获取所有的li标签下面的a标签：//li/a
ass=element.xpath('//li/a')
print(ass)
# 4.获取倒数第二li标签下面的a标签的文本：//li[last()-1]/a
ass=element.xpath('//li[last()-1]/a')[0]
# 获取text属性
print(ass.text)
# 4.2 通过xpath直接获取//li[last()-1]/a/text()
# 返回的是个列表
ass=element.xpath('//li[last()-1]/a/text()')[0]
print(ass)