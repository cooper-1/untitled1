# -*-coding:  utf-8 -*-
# @Time    :  2021/1/1 15:42
# @Author  :  Cooper
# @FileName:  多线程爬虫.py
# @Software:  PyCharm

import threading #使用线程库
import time
from queue import Queue #队列
import requests #请求处理
import json #json处理
import re
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import os
import urllib
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

class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        threading.Thread.__init__(self)
        # super(ThreadCrawl,self).__init__()
        self.threadName = threadName #线程名
        self.pageQueue = pageQueue #页码队列
        self.dataQueue = dataQueue #数据队列
        #请求报头
        self.header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        self.proxy = random.choice(proxylist)

    def run(self):
        print("启动 "+self.threadName)
        while not CRAWL_EXIT:
            try:
                ##从dataQueue中取出一个页码数字，先进先出
                #可选参数block,默认值是True
                #如果队列为空，block位True的话，不会结束，会进入阻塞状态，直到队列有新的数据
                #如果队列为空，block为False的话，就弹出一个Queue.empty()异常
                page = self.pageQueue.get(False)
                # 构建网页的URL地址
                url = 'https://search.bilibili.com/article?keyword=%E7%BE%8E%E5%9B%BE&page={}'.format(page)
                # print(url)
                # 请求报头
                header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
                proxy = random.choice(proxylist)
                res = requests.get(url, headers=self.header, proxies=self.proxy, timeout=10)
                print('第%s次·第一次网络状态码：' % page, res.status_code)
                # print(res.content.decode('utf-8'))
                pattern = re.compile('class="article-item"><a href="(.*?)"', re.S)
                result = pattern.findall(res.text)
                print(result)
                for url in result:
                    url='https:' + url
                    print(url)
                    self.dataQueue.put(url)
            except HTTPError:
                print('httperror')
            except RequestException:
                print('reqerror')
            except ReadTimeout:
                print('time out')
            except Exception as e:
                print(e)

        print("结束 "+self.threadName)

class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,urlQueue):
        super(ThreadParse,self).__init__()
        # 线程名
        self.threadName = threadName
        # 数据队列
        self.dataQueue = dataQueue
        # 保存解析后数据的url
        self.urlQueue = urlQueue

    def run(self):
        print("启动"+self.threadName)
        while not PARSE_EXIT:
            try:
                url = self.dataQueue.get(False)
                self.parse(url)
            except Exception as e:
                print(e)
        print("结束" + self.threadName)

    def parse(self,url):
        try:
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            proxy = random.choice(proxylist)
            res = requests.get(url, headers=header, proxies=proxy, timeout=10)
            global y
            y+=1
            print('第%s次的第二网络状态码：'%y , res.status_code)
            pattern = re.compile('img data-src="(.*?)"', re.S)  # class="preview" href=
            result = pattern.findall(res.text)

            list2 = []
            for url in result:
                list2.append('https:' + url)
            for url in list2[1:-1]:
                self.urlQueue.put(url)
        except HTTPError:
            print('httperror')
        except RequestException:
            print('reqerror')
        except ReadTimeout:
            print('time out')
        except Exception as e:
            print(e)
#______________________________________________

class UrlParse(threading.Thread):
    def __init__(self, threadName, urlQueue):
        super(UrlParse, self).__init__()
        # 线程名
        self.threadName = threadName
        # 保存解析后数据的url
        self.urlQueue = urlQueue

    def run(self):
        print("启动" + self.threadName)
        while not URL_EXIT:
            try:
                url = self.urlQueue.get(False)
                self.parse(url)
            except Exception as e:
                print(e)
        print("结束" + self.threadName)

    def parse(self, url):
        try:
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            proxy = random.choice(proxylist)
            path = r'E:\B站\图片7'
            global i
            i = i + 1
            filename = path + '/' + str(i) + '.jpg'
            print('第%s次准备保存图片·' % i, url)
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

#______________________________________________

CRAWL_EXIT = False #采集网页页码队列是否为空的信号
PARSE_EXIT = False #网页源码队列是否为空的信号
URL_EXIT = False #url队列是否为空的信号

def main():
    #页码队列，存储10个页码，先进先出
    pageQueue = Queue(10)
    #放入1~10的数字，先进先出
    for i in range(1,11):
        pageQueue.put(i)

    # 采集结果（网页的HTML源码的URL）的数据队列，参数为空表示不限制
    dataQueue = Queue()
    # 采集结果（第二次的URL）的数据队列，参数为空表示不限制
    urlQueue = Queue()

    #三个采集线程的名字
    crawlList = ["采集线程1号","采集线程2号","采集线程3号"]

    #创建、启动和存储三个采集线程
    threadCrawls = []
    for threadName in crawlList:
        thread = ThreadCrawl(threadName,pageQueue, dataQueue)
        thread.start()#线程开始
        threadCrawls.append(thread)

    # 三个解析线程的名字
    parseList = ["解析线程1号","解析线程2号","解析线程3号","解析线程4号","解析线程5号"]  # 创建、启动和存储三个解析线程

    threadParses = []
    for threadName in parseList:
        thread = ThreadParse(threadName,dataQueue,urlQueue)
        thread.start()
        threadParses.append(thread)

    # 9个第二次解析URL下载图片的线程名字
    urlList = ["第二次解析线程1号", "第二次解析线程2号", "第二次解析线程3号",
               "第二次解析线程4号", "第二次解析线程5号", "第二次解析线程6号",
               "第二次解析线程7号", "第二次解析线程8号", "第二次解析线程9号"]  #  创建、启动和存储三个解析线程
    UrlParses = []
    for threadName in urlList:
        thread = UrlParse(threadName, urlQueue)
        thread.start()
        UrlParses.append(thread)

    while not pageQueue.empty():
        pass
    #如果pageQueue为空，采集线程退出循环
    global  CRAWL_EXIT
    CRAWL_EXIT = True
    print("pageQueue为空")
    for thread in threadCrawls:
        thread.join() #阻塞子线程
        print("1")

    while not dataQueue.empty():
        pass
    # 如果 dataQueue空，解析线程退出循环
    print("dataQueue为空")
    global PARSE_EXIT
    PARSE_EXIT = True
    for thread in threadParses:
        thread.join()
        print("2")

    while not urlQueue.empty():
        pass
    # 如果 dataQueue空，解析线程退出循环
    print("urlQueue为空")
    global URL_EXIT
    URL_EXIT = True
    for thread in UrlParses:
        thread.join()
        print("3")


if __name__ == "__main__":
    #main()
    #性能测试
    startTime = time.time()
    main()
    print(time.time() - startTime)