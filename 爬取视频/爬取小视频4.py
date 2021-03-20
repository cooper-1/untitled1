# -*-coding:  utf-8 -*-
# @Time    :  2021/2/2 21:09
# @Author  :  Cooper
# @FileName:  爬取小视频4.py
# @Software:  PyCharm


from gevent import monkey#把下面有可能有IO操作的单独做上标记
monkey.patch_all()#将IO转换为异步执行的函数
"""也就是说，我们要先引用多协程模块monkey.patch_all()，再引用别的才行，不然会报错"""
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import re
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import urllib3
import gevent
from gevent.queue import Queue
from gevent.lock import BoundedSemaphore
sem = BoundedSemaphore(1)
import sys
sys.setrecursionlimit(1000000)  # 例如这里设置为一百万
urllib3.disable_warnings()

i=0
i2=0
j=0
k=0
urllist=[]
urllist2=[]
urllist3=[]

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

proxylist=[{"https":"https://83.166.111.67:9999"},	{"http":"http://183.166.70.242:9999"},]

def getlist(url):
    # 获取列表URL
    # try:

        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('第%s轮，第一次·网络状态码: '%i,res.status_code)
        #print(res.content.decode('utf-8'))
        pattern = re.compile('<li><a href="/voddetail/(.*?)\.html" title="*?', re.S)  # <img class="" src=
        result = pattern.findall(res.text)
        print(result)#https://yinghuaav.site/voddetail/42483.html
        for url in result:
            url = 'https://yinghuaav.site/vodplay/%s-1-1.html'%url
            urllist.append(url)
        print(urllist)

    # except HTTPError:
    #     print('httperror')
    # except RequestException:
    #     print('reqerror')
    # except ReadTimeout:
    #     print('time out')
    # except Exception as e:
    #     print(e)
def indexlist(url):
    # 创建option对象
    option = Options()
    # 设置选项为无界面
    option.headless = True
    # 使用option配置chrome浏览器
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    #time.sleep(2)
    a=driver.find_elements_by_tag_name('iframe')
    # for a1 in a[1:]:
    #     #print(a1.text)
    print(a[2].get_attribute('src'))
    url=(a[2].get_attribute('src')).split('=')[-1]
    print(url)
    urllist2.append(url)
    driver.quit()

def index2list(k):
    print('协程开始*************************%s' % k)
    while not workQueue.empty():
        url = workQueue.get(timeout=2)
        urllist5=[]
        global j
        j+=1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        # proxy ={'http': 'http://59.29.245.151:3128'}
        res = requests.get(url, headers=header, verify=False, timeout=10)
        print('第%s轮，第一次·网络状态码: ' % j, res.status_code)
        #print(res.content.decode('utf-8'))
        pattern = re.compile('/202(.*?)\.ts', re.S)  # <img class="" src=
        result = pattern.findall(res.text)
        #print(result)
        for url in result:
            url='https://lbbf9.com/202%s.ts'%url
            #print(url)
            urllist5.append(url)
        print('',urllist5)
        print(len(urllist5))
        down(urllist5,k)

def down(urllist5,kk):
    x=0
    for url in  urllist5:
        try:
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            #proxy = random.choice(proxylist)
            path = r'E:\视频\小电影'
            filename = path + '/' + str(url.split('/')[-4]) + '1.ts'
            x=x+1
            print('协程%s第%s次准备保存视频片段·' % (kk,x), url)
            with open(filename, 'ab') as f:
                f.write(requests.get(url, headers=header, timeout=30).content)
        except HTTPError:
            print('httperror')
        except RequestException:
            print('reqerror')
        except ReadTimeout:
            print('time out')
        except Exception as e:
            print(e)
        finally:
            pass


def boss():
    # 填充队列
    global i2
    for url in urllist2:
        #print('原', url)
        url = url.replace('index', '700kb/hls/index')
        print(url)
        i2 = i2 + 1
        workQueue.put_nowait(url)
    print('有%s个视频 ' % i2)


if __name__ == "__main__":
    startTime = time.time()
    workQueue = Queue()
    for b in range(8,9):
        url = 'https://yinghuaav.site/vodtype/27-%s.html'%b
        getlist(url)
        for url in urllist:
          indexlist(url)#url='https://lbbf9.com/20200623/LCB1td1k/index.m3u8'
        print('urllist2',urllist2)

        print("Started processes")
        # 创建一个协程任务
        gevent.spawn(boss).join()
        jobs = []
        for k2 in range(24):
            # 保存所有的协程任务
            jobs.append(gevent.spawn(index2list, k2))
        # joinall()接收一个列表，将列表里的所有协程任务添加到任务队列里执行
        gevent.joinall(jobs)
        print("Main process Ended")

    print(time.time() - startTime)