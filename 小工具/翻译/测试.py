# -*-coding:  UTF-8
# @Time    :  2021/7/16 19:19
# @Author  :  Cooper
# @FileName:  测试.py
# @Software:  PyCharm
if '' == None:
    print('ok')
if '' == False:
    print('ok')
if None == False:
    print('ok')
if [] == False:
    print('ok')
if [] == None:
    print('ok')
if [] == '':
    print('ok')
if set() == False:
    print('ok')

if not set():
    print('ok1')
if not '':
    print('ok1')
if not []:
    print('ok1')
if [] == {}:
    print('ok2')
if 0 == {}:
    print('ok2')
