# -*-coding:  utf-8 -*-
# @Time    :  2021/2/23 17:16
# @Author  :  Cooper
# @FileName:  test10.py
# @Software:  PyCharm
a={1}
print(type(a))
a=set([1,8,3,11])
b=set({1,8,3,11,1})
c={}
print(a is b)
print(b)
print(type(c))
for x in a:
    print(x)
print(sorted(a))
a.add(5)
for x in a:
    print(x)
print(sorted(a))
c=[1,2,3]
print(3 in c)
d={'sdfsjdf','a','f','fsaf','a'}
print(d)
print(0 and 10)
print(None or  'adjashds')