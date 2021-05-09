# -*-coding:  utf-8 -*-
# @Time    :  2021/3/7 15:47
# @Author  :  Cooper
# @FileName:  test3.py
# @Software:  PyCharm
x=None;y=20;print(x and y)
x=10;y=20;print(x or y)
print(False==0)
print(False==[])
print(0==[])
if not []:
    print('jgjghfhgf')
if not 0:
    print('jgjghfhg')
if not False:
    print(0.1+0.2)
if not None:
    print(1+0.2)
def Add(x,y):
    print('55757')
    print(x + y)
    return x+y,x-y,x/y
a,b,c=Add(7,8)
print(a,b,c)
def people(name='小孩',age=15,address='北京'):
    print('名字：',name)
    print('年龄：',age)
    print('地址：',address)

people(address='xxx',age='jjj',)

str1 = 'fhdsgfjhgsdfjhgsdjfhgjdsfgjd'
# num=eval(input('请输入一个整数'))
# print(str1[num])
try:

    num=eval(input('请输入一个整数'))
    print(str1[num])
except NameError:
        print('命名错误')
except Exception as e:
        print(e)

else:
    print('success')


