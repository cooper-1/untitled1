# -*-coding:  UTF-8
# @Time    :  2021/5/22 20:16
# @Author  :  Cooper
# @FileName:  test.py
# @Software:  PyCharm
b={'4':'d','5':'e','6':'f'}
a={1:'a','2':'b','3':'c'}
print(a.update(b))
c = a.update(b)
print(a)
print(type(c))
print({1:'a',2:'a',3:'a'}.update({4:'a',5:'a',6:'a'}))
A = {'a': 11, 'b': 22}
B = {'c': 48, 'd': 13}
#update() 把字典B的键/值对更新到A里

print(A.update(B))
print(A)
