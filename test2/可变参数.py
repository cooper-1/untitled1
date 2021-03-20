# -*-coding:  utf-8 -*-
# @Time    :  2021/3/8 16:21
# @Author  :  Cooper
# @FileName:  可变参数.py
# @Software:  PyCharm
def test(a,b,c=1,*p,**k):
    print('a=',a,'b=',b,'c=',c,'p=',p,'k=',k)

test(3,4)
test(3,4,5)
test(3,4,5,x=7,y=8)
test(3,4,5,'a','b',x=7,y=8)
test(3,4,5,'ab',x=7,y=8)
a=4
# print(dir(a))
import os
import csv
# os.mkdir('abc.txt')
print(os.listdir())
# f=open('test.csv','w')
# lis=['北京','上海','tianjing','杭州']
# f.write(','.join(lis))
# f.close()
f=open('test.csv','r')
lis=[['北京','上海','tianjing','杭州'],['1','2','tianjing','4'],
     ['a','b','tianjing','d'],['ad','上e','tianjing','o州'],]
print(f.read().split(','))
f.close()
f=open('test2.csv','w', newline='')
w = csv.writer(f)#方式一
w.writerows(lis)
for row in lis:
    w.writerow(row)
    w.writerows([row])
    w.writerow(['dfjgh','ghfdg','abcdef','ghijk'])
for row in lis:
    f.write(','.join(row)+'\n')
f.close()