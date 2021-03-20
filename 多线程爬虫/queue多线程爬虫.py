# -*-coding:  utf-8 -*-
# @Time    :  2021/1/17 22:08
# @Author  :  Cooper
# @FileName:  queue多线程爬虫.py
# @Software:  PyCharm

import threading #使用线程库
import time
import  queue as Queue
import requests #请求处理
import re
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import os
import random

user_agent_list = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19                                                      *                                   .0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

proxylist=[
	{"http":"http://175.43.130.154:9999"},
	{"http":"http://183.166.20.129:9999"},
	{"http":"http://106.110.195.3:9999"},
	{"http":"http://175.44.108.75:9999"},
	{"http":"http://49.86.26.166:9999"},
	{"http":"http://113.121.37.248:9999"}
]

i=0#用来计数
y=0#用来计数
j=0#用来计数

class myThread(threading.Thread):
    def __init__(self,name,q):
        threading.Thread.__init__(self)
        self.name=name
        self.q=q
    def run(self) :
        print("Starting" +self.name)
        while True:
            try:
                crawler(self.name,self.q)
            except:
                break
        print("Exited" + self.name)
def  crawler(threadName,q):
    url=q.get(timeout=2)
    try:
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        proxy = random.choice(proxylist)
        path = r'E:\B站\图片13'
        global j
        j = j + 1
        filename = path + '/' + str(j) + '.jpg'
        print('第%s次准备保存图片·' % j, url)
        with open(filename, 'wb') as f:
            f.write(requests.get(url, proxies=proxy, headers=header, timeout=30).content)
    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    startTime = time.time()
    threadList=["Thread-1","Thread-2","Thread-3","Thread-4","Thread-5"]
    workQueue=Queue.Queue()
    threads=[]
    #创建新线程
    for tName in threadList:
        thread=myThread(tName,workQueue)
        thread.start()
        threads.append(thread)

    urllist = []
    with open('url.txt', 'r') as file:
        file_list = file.readlines()
        for eachone in file_list:
            # print(eachone)
            link = eachone.split('\t')[0]
            i += 1
            if i==101:
                break
            link = link.replace('\n', '')
            #print(link)
            urllist.append(link)
        print(urllist,'\n',i)

        print("Started processes")

        # 填充队列
        for url in urllist:
            workQueue.put(url)
           # print(url)

        #等待所有线程完成
        for t in threads:
            t.join()

        print("Main process Ended")
        print(time.time() - startTime)

#57.4秒