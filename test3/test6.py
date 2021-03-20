# -*-coding:  utf-8 -*-
# @Time    :  2021/3/18 16:59
# @Author  :  Cooper
# @FileName:  test6.py
# @Software:  PyCharm
def fun(n:int):
    if n>0:
        return n*fun(n-1)
    else:
        return 1
a=fun(5)
print(a)