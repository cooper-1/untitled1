# -*-coding:  utf-8 -*-
# @Time    :  2021/2/12 19:52
# @Author  :  Cooper
# @FileName:  test2.py
# @Software:  PyCharm
class Father():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dev(self):
        return self.a - self.b


# 调用父类初始化参数a,b并增加额外参数c
class Son(Father):
    def __init__(self, a, b, c=100):  # 固定值： 例如默认c=10，也可以显式地将c赋值
        Father.__init__(self, a, b)
        self.c = 10

    def add(self):
        return self.a + self.b

    def compare(self):
        if self.c > (self.a + self.b):
            return True
        else:
            return False


son = Son(1, 2)  # 显式地将c=1传入子类初始化函数
print(son.dev())  # 调用父类dev函数
print(son.add())  # 子类自身add函数
print(son.a)  # 子类自身add函数
print(son.c)  # 子类自身add函数
print(son.compare())  # 子类自身compare函数