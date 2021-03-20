# -*-coding:  utf-8 -*-
# @Time    :  2021/1/18 17:36
# @Author  :  Cooper
# @FileName:  多线程+多协程2.py
# @Software:  PyCharm

from gevent import monkey;
import gevent
monkey.patch_all()
from threading import Thread
import time
import requests #请求处理
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import random
import  queue
from gevent.queue import Queue,Empty

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

i=0#计数
j=0
l=0
i1=0
url_list = []

def crawl(k):
    global i1
    i1+=1
    print("协程——————",i1)
    try:
        while not workQueue.empty():
            url = workQueue.get(timeout=2)
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            proxy = random.choice(proxylist)
            path = r'E:\B站\图片14'
            global j
            j = j + 1
            filename = path + '/' + str(j) + '.jpg'
            print('第%s次准备保存图片·' % j, url)
            with open(filename, 'wb') as f:
                f.write(requests.get(url, proxies=proxy, headers=header, timeout=50).content)
            global l
            l = l + 1
            print('第%s次保存图片·OK' % l)

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)

def task_gevent(queue,s):
    url_list = []
    while not queue.empty():
        url = queue.get()
        url_list.append(url)
        if len(url_list) >= ((i-1)/5-1):
            print(len(url_list))
            # 创建一个协程任务
            gevent.spawn(boss(url_list)).join()
            jobs = []
            for k in range(5):#最多5条线程乘以各5条协程=25条协程
                # 保存所有的协程任务
                jobs.append(gevent.spawn(crawl, k))
            # joinall()接收一个列表，将列表里的所有协程任务添加到任务队列里执行
            gevent.joinall(jobs)
            url_list = []
    if url_list :#如果不能整除列表还有剩，单独开一条协程
        jobs = []
        gevent.spawn(boss(url_list)).join()
        jobs.append(gevent.spawn(crawl, 26))
        gevent.joinall(jobs)
        url_list = []

def boss(url_list):
    # 填充队列
    for url in url_list:
        workQueue.put_nowait(url)


if __name__ == '__main__':
    workQueue = Queue()
    queue = queue.Queue()
    urllist = []
    with open('url.txt', 'r') as file:
        file_list = file.readlines()
        for eachone in file_list:
            link = eachone.split('\t')[0]
            i += 1
            if i == 301:
                break
            link = link.replace('\n', '')
            urllist.append(link)
        print(urllist, '\n', i)

    for url in urllist:
            queue.put(url)

    start = time.time()
    print("********************** 开始计时 **********************")
    t_list = []
    for s in range(5):
        t = Thread(target=task_gevent, args=(queue,s)) #多进程 + 协程
        t.start()
        t_list.append(t)
        print(t)
    for p in t_list:
        p.join()
        print(p)

    end = time.time()
    print("********************** 结束计时 **********************")
    print("总耗时：",end - start)
    # 300张图片159.4