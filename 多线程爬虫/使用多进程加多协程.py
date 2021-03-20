
from gevent import monkey#把下面有可能有IO操作的单独做上标记
monkey.patch_all()#将IO转换为异步执行的函数
"""也就是说，我们要先引用多协程模块monkey.patch_all()，再引用别的才行，不然会报错"""
import threading #使用线程库
from queue import Queue #队列
import re
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import os
from multiprocessing import  Process,Queue
import time
import requests,random
import gevent
from gevent.queue import Queue as queue1
from gevent.queue import Empty


import sys
sys.setrecursionlimit(1000000)  # 例如这里设置为一百万

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


i=0
j=0

class Myprocess(Process):
    def __init__(self,q):
        Process.__init__(self)
        self.q=q

    def run(self):
        print("进程开始", self.pid)
        while not self.q.empty():
            crawler1(self.q)
        print("进程结束", self.pid)


def crawler1(q):
    print("进入协程")
    gevent.spawn(boss).join()
    jobs = []
    for k in range(5):
        # 保存所有的协程任务
        jobs.append(gevent.spawn(crawler, k))
    # joinall()接收一个列表，将列表里的所有协程任务添加到任务队列里执行
    gevent.joinall(jobs)


def boss(q):
    # 重新分配队列

    while not workQueue.empty():
        url = workQueue.get(timeout=2)
        if (k==10):
            break
        workQueue2.put_nowait(url)



def crawler(index):
    Process_id="process---"+str(index)
    print(Process_id)
    try:
        while not workQueue2.empty():
            url=workQueue2.get(timeout=2)
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            proxy = random.choice(proxylist)
            path = r'E:\B站\图片14'
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
    workQueue=Queue()
    workQueue2=Queue()

    urllist = []
    with open('url.txt', 'r') as file:
        file_list = file.readlines()
        for eachone in file_list:
            # print(eachone)
            link = eachone.split('\t')[0]
            i += 1
            if i==251:
                break
            link = link.replace('\n', '')
            #print(link)
            urllist.append(link)
        print(urllist,'\n',i)

    # 填充队列
    for url in urllist:
        workQueue.put(url)

    for i in range(5):
        p = Myprocess(workQueue)
        p.daemon = False
        p.start()
        p.join()

    print("Main process Ended")
    print(time.time() - startTime)
