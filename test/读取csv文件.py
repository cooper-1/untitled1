# -*-coding:  utf-8 -*-
# @Time    :  2021/3/6 12:59
# @Author  :  Cooper
# @FileName:  读取csv文件.py
# @Software:  PyCharm
import pandas as pd                         #导入pandas包
data = pd.read_csv("text2.csv")           	#读取csv文件
print(data[:5])                                #打印所有文件
print(data.head(6))                                #打印所有文件
print(type(data))
print(data.columns) 						#返回全部列名

print(data.shape)							#f返回csv文件形状

print(data.loc[1:2])						#打印第1到2行
print('——'*20)
a=data.loc[0:4, ['番剧名称']]       #打印行中特定列
print(a)#打印所有文件
print(type(a))#打印所有文件
import numpy as np
data = np.array(a)
# print(data)
print(type(data))
for da in data:
        print(da[0])
