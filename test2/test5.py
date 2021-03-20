# -*-coding:  utf-8 -*-
# @Time    :  2021/3/8 12:13
# @Author  :  Cooper
# @FileName:  test5.py
# @Software:  PyCharm
import re
s="大家好，我是一个av18cd程序员小白。I 'm so glad to introduce myself, and I’m 18 years old.   Today is 2020/01/01. It is a wonderful DAY! @HHHHello,,,#111ComeHere222...66？AA？zz？——http://welcome.cn"
print(re.sub(r'[0-9]', '*', s))
print(re.sub(r'[^0-9]+', '*', s))

s="大家好，我是一个程序员小白。I 'm so glad to introduce myself, and I’m 18 years old.   Today is 2020/01/01. It is a wonderful DAY! @HHHHello,,,#111ComeHere222...66？AA？zz？——http://welcome.cn"
print(s)
print(re.sub(r'http[:]\S+', '', s))


