# -*-coding:  utf-8 -*-
# @Time    :  2021/2/4 12:11
# @Author  :  Cooper
# @FileName:  爬取加密视频.py

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
from Crypto.Cipher import AES
from gevent.queue import Queue
from agency.MergeFile import merge,delete
import sys
sys.setrecursionlimit(1000000)  # 例如这里设置为一百万
urllib3.disable_warnings()

i=0
i2=0
j=0
j2=0
j3=0
k=0
k2=0
urllist=[]
keyurl=''
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
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

def getlist(url):
    # 获取列表URL
    try:

        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('第%s轮，第一次·网络状态码: '%i,res.status_code)
        #print(res.content.decode('utf-8'))
        pattern = re.compile('<a href="/vod-detail-id-(\d*?).html" title="*?', re.S)  # <img class="" src=
        result = pattern.findall(res.text)
        print(result)
        #https://4096av.live/vod-detail-id-23057.html
        #https://4096av.live/vod-view-id-23057.html
        for url in result:
            url = 'https://4096av.live/vod-view-id-%s.html'%url
            urllist.append(url)
        print(urllist)

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)
def indexlist(url):
    # 创建option对象
    option = Options()
    # 设置选项为无界面
    option.headless = True
    # 使用option配置chrome浏览器
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    #print(driver.page_source)
    pattern = re.compile('"source": "(.*?)"', re.S)  # <img class="" src=
    result = pattern.findall(driver.page_source)
    print(result[0])
    #https://www.fhbf9.com/20201217/IYuiIaRG/index.m3u8
    urllist2.append(result[0])
    driver.quit()

def index2list(url):
    global j,keyurl,urllist3
    urllist3 = []
    j+=1
    header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
    # proxy ={'http': 'http://59.29.245.151:3128'}
    res = requests.get(url, headers=header, verify=False, timeout=20)
    print('第%s轮，第一次·网络状态码: ' % j, res.status_code)
    #print(res.content.decode('utf-8'))
    pattern = re.compile('METHOD=AES-128,URI="(.*?)"', re.S)  # <img class="" src=
    result = pattern.findall(res.text)
    print(result[0])#/20201217/IYuiIaRG/800kb/hls/key.key
    #https://www.fhbf9.com/20201217/IYuiIaRG/800kb/hls/key.key

    keyurl='https://www.fhbf9.com'+result[0]
    print(keyurl)
    pattern = re.compile('/800kb/hls/(\w*?)\.ts', re.S)  # <img class="" src=
    result = pattern.findall(res.text)
    print(result)
    for tx in result:
        #https://www.fhbf9.com/20201217/IYuiIaRG/800kb/hls/index.m3u8
        #https://www.fhbf9.com/20201217/IYuiIaRG/800kb/hls/3MpjY5Y6.ts

        url1=url.replace('index.m3u8',tx)+'.ts'
        #print(url1)
        urllist3.append(url1)
    print('urllist3',urllist3)
    print(len(urllist3))

def down(k,path):
    global keyurl
    print('协程开始*************************%s' % k)
    try:
        key = requests.get(keyurl).content
        cryptor = AES.new(key, AES.MODE_CBC, key)  # 通过AES对ts进行解密
        while not workQueue.empty():
            url = workQueue.get(timeout=2)
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            #path = r'E:\视频\电影'
            filename = path + '/' + str(url.split('/')[-4]) + '.ts'
            #sem.acquire()#加锁
            global j2
            j2+= 1
            #filename = path + '/' + str(url.split('/')[-4]) + '.ts'
            filename = path + '/' + str(j2) + '.ts'
            print('第%s轮的第%s次准备保存视频片段·' % (j3,j2), url)
            with open(filename, 'ab') as f:
                #f.write(cryptor.decrypt(resp.content))
                f.write(cryptor.decrypt(requests.get(url, headers=header, timeout=10).content))

           # sem.release()#锁释放
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
    global i2,urllist3
    for url in urllist3:
        i2=i2+1
        workQueue.put_nowait(url)
    print('有%s段视频'%i2)
    #urllist3=[]


if __name__ == "__main__":
    startTime = time.time()
    workQueue = Queue()
    path = r'E:\视频\加密电影'

    url = 'https://4096av.live/vod-type-5-4.html'
    #url = 'https://4096av.live/vod-view-id-22247.html'

    getlist(url)
    for url in urllist[4:6]:
        indexlist(url)
    print('urllist2', urllist2)
    for url in urllist2:
        url = url.replace('index', '800kb/hls/index')
        # https://www.fhbf9.com/20201217/IYuiIaRG/index.m3u8
        # https://www.fhbf9.com/20201217/IYuiIaRG/800kb/hls/index.m3u8
        print('url=====',url)
        index2list(url)
        print('urllist32', urllist3)
        #______________________
        # key = requests.get(keyurl).content
        # cryptor = AES.new(key, AES.MODE_CBC, key)  # 通过AES对ts进行解密
        #______________________

        print("Started processes")
        j3 += 1
        # 创建一个协程任务
        gevent.spawn(boss).join()
        jobs = []
        for k2 in range(15):
            # 保存所有的协程任务
            jobs.append(gevent.spawn(down, k2,path))
        # joinall()接收一个列表，将列表里的所有协程任务添加到任务队列里执行
        gevent.joinall(jobs)
        name = url.split('/')[-4]
        merge(path, name)  # 合并文件
        delete(path)  # 删除小文件
        j2 = 0
        urllist3 = []
        keyurl=''
        key=''
        #gevent.killall()
        print("Main process Ended")
    print(time.time() - startTime)
    #https://vip1.fhbf9.com/20210110/IUz6flj9/800kb/hls/index.m3u8