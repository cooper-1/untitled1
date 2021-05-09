# -*-coding:  utf-8 -*-
# @Time    :  2021/3/7 14:07
# @Author  :  Cooper
# @FileName:  test.py
# @Software:  PyCharm
url = '//search.bilibili.com/article?keyword=p%E7%AB%99'
print(url[:2])
si=3.1415926
print(type(si))
des=round(si,2)
print(des)
print('{:.3}'.format(3.111))
print('{:.2f}'.format(30.1415926))
physics=eval(input('请输入物理成绩'))
biology=eval(input('请输入生物成绩'))
chemistry=eval(input('请输入化学成绩'))
average=(physics+biology+chemistry)/3
print('{:.2f}'.format(average))