# -*-coding:  utf-8 -*-
# @Time    :  2021/3/18 17:09
# @Author  :  Cooper
# @FileName:  tesst6.py
# @Software:  PyCharm
def fun1(param1: int, param2: int):
    """
    :param x:int:param1 int:param2
    :return: 返回一个函数，该函数接受一个数字列表，返回两个列表，其中第一个列表中全是小于param1的数字，第二个列表全是大于param2的数字
    """
    def fun(lis):
        if type(lis)==type([]):
            pass
        else:
            raise TypeError
        lis1 = []
        lis2 = []
        nonlocal param1,param2
        # param = 10
        # param2 = 20
        for i in lis:
            if i<param1:
                lis1.append(i)
            elif i>param2:
                lis2.append((i))
        return lis1,lis2

    return fun
num=[20,50,15,14,1,2,3]
a=fun1(10,20)
b,c=a(num)
print(b,c)

