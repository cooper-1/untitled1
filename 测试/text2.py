# -*-coding:  utf-8 -*-
# @Time    :  2021/1/1 15:03
# @Author  :  Cooper
# @FileName:  text2.py
# @Software:  PyCharm

import threading
import  time

class myThread(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name=name
        self.delay=delay
    def run(self):
        print("Strating"+self.name)
        print_time(self.name,self.delay)
        print("Exiting"+self.name)
def print_time(threaName,delay):
    counter=0
    while counter<3:
        time.sleep(delay)
        print(threaName,time.ctime())
        counter+=1


threads=[]
#创建新线程
thread1=myThread("线程1",1)
thread2=myThread("线程2",2)

#开启新线程
thread1.start()
thread2.start()

#添加线程到列表
threads.append(thread1)
threads.append(thread2)

#等待所有线程完成
# for t in threads:
#     print("t=======",t)
#     t.join()
#     print("结束")

print("Exiting Main threading")
