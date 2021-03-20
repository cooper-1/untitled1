# -*-coding:  utf-8 -*-
# @Time    :  2021/1/30 14:33
# @Author  :  Cooper
# @FileName:  爬取B站评论.py
# @Software:  PyCharm

from gevent import monkey#把下面有可能有IO操作的单独做上标记
monkey.patch_all()#将IO转换为异步执行的函数
"""也就是说，我们要先引用多协程模块monkey.patch_all()，再引用别的才行，不然会报错"""
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import os
import re
import random
import gevent
from gevent.queue import Queue
import agency.proxies
from agency.kdlproxies import   Proxy

import sys
sys.setrecursionlimit(100000)  # 例如这里设置为10万
i=1
i2=0
i3=0
j = 0

urllist=[]#存取URL的列表
urllist2=[]#存取URL的列表

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
    ": Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", \
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

def getlist(url):
    # 获取列表URL
    try:
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        proxy = random.choice(proxylist)  # 随机选一个ip地址
        res = requests.get(url, headers=header,proxies=proxy,timeout=10)
        print('第%s轮，第一次·网络状态码： '%i,res.status_code)
        print(res.content.decode('utf-8'))

        # pattern = re.compile('<a target="_blank" href="(.*?)" title="*?', re.S)  # <img class="" src=
        # result=pattern.findall(res.text)
        # #print(result)
        # for url in result:
        #     url='https://t2cy.com'+url
        #     urllist.append(url)
        # print(urllist)

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


def image(k):
    print('协程2开始______________________________%s' % k)
    while not workQueue2.empty():
        try:
            url = workQueue2.get(timeout=2)
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            proxy = random.choice(proxylist)  # 随机选一个ip地址
            res = requests.get(url, headers=header,proxies=proxy,timeout=10)
            #print(res.content.decode('utf-8'))
            pattern = re.compile('<img class="lazy" data-loadsrc="(.*?)" alt=*?', re.S)  # <img class="" src=
            result=pattern.findall(res.text)
            #print(result)
            for url in result:
                url='https://t2cy.com'+url
                urllist2.append(url)
            #print(urllist2)

        except HTTPError:
            print('httperror')
        except RequestException:
            print('reqerror')
        except ReadTimeout:
            print('time out')
        except Exception as e:
            print(e)

def down(k):
    print('协程开始*************************%s' % k)
    while not workQueue.empty():
        try:
            url = workQueue.get(timeout=2)
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            proxy = random.choice(proxylist)
            path = r'E:\B站\图片22'
            global j
            j = j + 1
            filename = path + '/' + str(j) + '.jpg'
            print('第%s次准备保存图片·' % j, url)
            with open(filename, 'wb') as f:
                f.write(requests.get(url, proxies=proxy, headers=header, timeout=10).content)
        except HTTPError:
            print('httperror')
        except RequestException:
            print('reqerror')
        except ReadTimeout:
            print('time out')
        except Exception as e:
            print(e)
def boss():
    # 填充队列
    global i2
    for url in urllist2:
        i2=i2+1
        workQueue.put_nowait(url)
    print('有%s张图片'%i2)


def boss2():
    # 填充队列
    global i3
    for url in urllist:
        i3=i3+1
        workQueue2.put_nowait(url)
    print('有%s张图集'%i3)

if __name__ == "__main__":
    workQueue = Queue()
    workQueue2 = Queue()
    url = 'https://www.bilibili.com/bangumi/play/ss1650/?from=search&seid=8499675616148596941'
    #url = 'https://t2cy.com/acg/daily/index_2.html'
    getlist(url)
    #
    # for i in range(2,4):
    #     url = 'https://t2cy.com/acg/daily/index_%s.html'%i
    #     getlist(url)
    #
    # print("Started processes2")
    # # 创建一个协程任务
    # gevent.spawn(boss2).join()
    # jobs = []
    # for k in range(25):
    #     # 保存所有的协程任务
    #     jobs.append(gevent.spawn(image, k))
    # # joinall()接收一个列表，将列表里的所有协程任务添加到任务队列里执行
    # gevent.joinall(jobs)
    # print("Main process Ended2")
    #
    # print("Started processes")
    # # 创建一个协程任务
    # gevent.spawn(boss).join()
    # jobs = []
    # for k in range(25):
    #     # 保存所有的协程任务
    #     jobs.append(gevent.spawn(down, k))
    # # joinall()接收一个列表，将列表里的所有协程任务添加到任务队列里执行
    # gevent.joinall(jobs)
    # print("Main process Ended")
