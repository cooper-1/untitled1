# -*-coding:  utf-8 -*-
# @Time    :  2021/2/2 19:42
# @Author  :  Cooper
# @FileName:  爬取小视频3.py
# @Software:  PyCharm

import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import re
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import urllib3
urllib3.disable_warnings()

i=0
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

def index2list(url):
    print(url)
    global j
    j+=1
    header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
    # proxy ={'http': 'http://59.29.245.151:3128'}
    res = requests.get(url, headers=header, verify=False, timeout=20)
    print('第%s轮，第一次·网络状态码: ' % j, res.status_code)
    #print(res.content.decode('utf-8'))
    pattern = re.compile('/20(.*?)\.ts', re.S)  # <img class="" src=
    result = pattern.findall(res.text)
    #print(result)
    for url in result:
        url='https://lbbf9.com/20%s.ts'%url
        #print(url)
        urllist3.append(url)
    print(urllist3)
    print(len(urllist3))

def down(urllist3):
    for url in  urllist3:
        try:
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            #proxy = random.choice(proxylist)
            path = r'E:\视频\小电影'
            global k
            k = k + 1
            filename = path + '/' + str(url.split('/')[-4]) + '1.ts'
            print('第%s次准备保存视频片段·' % k, url)
            with open(filename, 'ab') as f:
                f.write(requests.get(url, headers=header, timeout=10).content)
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


if __name__ == "__main__":
    startTime = time.time()
    url = 'https://yinghuaav.site/vodtype/31-3.html'
    getlist(url)
    for url in urllist[-3:-2]:
    # url='https://yinghuaav.site/vodplay/42483-1-1.html'
      indexlist(url)#url='https://lbbf9.com/20200623/LCB1td1k/index.m3u8'
    print('urllist2',urllist2)

    # url='https://lbbf9.com/20200623/LCB1td1k/%sindex.m3u8'%('700kb/hls/')#https://lbbf9.com/20200623/lNc5tcCf/700kb/hls/index.m3u8

    # print(url)
    for url in urllist2:
        print('原',url)
        url=url.replace('index','700kb/hls/index')
        print(url)
        index2list(url)
    #https://lbbf9.com/20200623/LCB1td1k/700kb/hls/index.m3u8
    #https://lbbf9.com/20200623/LCB1td1k/700kb/hls/bnrqoxod.ts
    down(urllist3)
    print(time.time() - startTime)