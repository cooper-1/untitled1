# -*-coding:  utf-8 -*-
# @Time    :  2021/1/27 17:24
# @Author  :  Cooper
# @FileName:  test4.py
# @Software:  PyCharm
for i  in range(10):
    for j  in range(10):
        for k  in range(10):
            print(k)
            for l in range(1,10):
                if l==k :
                    print(i,j,k,l)
                else:
                    break