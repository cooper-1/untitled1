# -*-coding:  utf-8 -*-
# @Time    :  2021/2/12 18:29
# @Author  :  Cooper
# @FileName:  test.py
# @Software:  PyCharm

class farther(object):
    def __init__(self):
        self.x = '这是属性'

    def fun(self):
        print(self.x)
        print('这是方法')

class son(farther):
    def __init__(self):
        super(son, self).__init__()
        print('实例化执行')

test = son()
test.fun()
print(test.x)

class Father():
    def __init__(self):
        self.a = '这是属性'

    def action(self):
        print('调用父类的方法')
        print(self.a)

class Son(Father):
    print('实例化执行')
    pass

son = Son()  # 子类Son 继承父类Father的所有属性和方法
son.action()  # 调用父类方法
son.a  # 调用父类属性

