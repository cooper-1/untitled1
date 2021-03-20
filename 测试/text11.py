# -*-coding:  utf-8 -*-
# @Time    :  2021/2/10 1:04
# @Author  :  Cooper
# @FileName:  text11.py
# @Software:  PyCharm

import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import re
import os
import time
import random
import csv
requests.packages.urllib3.disable_warnings()

i=0
j=0
j2=0
j3=0
j4=0

urllist=[]
urllist2=[]

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
        global j
        j += 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('第%s轮，第一次·网络状态码: '%j,res.status_code)
        #print(res.content.decode('utf-8'))
        pattern = re.compile('<li logr="(.*?)  </li>', re.S)  # <img class="" src=
        result = pattern.findall(res.text)
        # print(result)
        for url in result:
            pattern = re.compile('href="(.*?)"\n', re.S)  # <img class="" src=
            url = pattern.findall(url)
            #print(url[0])
            urllist.append(url[0])
        print(urllist)
        print(len(urllist))

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


def getmessage(url):
    # 获取列表URL
    try:
        global j2
        j2+=1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('第%s轮，第二次·网络状态码: '%j2,res.status_code)
        #print(res.content.decode('utf-8'))
        path=r'E:\信息'
        if  not os.path.exists(path):
            os.makedirs(path)
        filename = path + '/' + '厂房2' + '.txt'
        with open(filename, 'ab') as f:
            print('准备保存信息片段·')
            pattern = re.compile('<h1 class="c_000 f20">\(出租\)&nbsp;(.*?)</h1>', re.S)  # 海沧东浮镇50000平标准物流仓库出租滴水12米双边库
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  。  '.encode())
            pattern = re.compile(' <span class="title">区&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;域：</span>\n                    (.*?)                </p>', re.S)  # 海沧
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="address">(.*?)</span>', re.S)  # 海沧东孚
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="up">(\d*?)m²</span>', re.S)  # 5000m²
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="house_basic_title_money_num_second">(.*?)元/m²/天&nbsp;&nbsp;&nbsp;&nbsp;', re.S)  # 0.9
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="house_basic_title_money_num">(.*?)</span>', re.S)  # 135
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="house_basic_title_money_unit">(.*?)</span>', re.S)  # 单位
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                f.write(result[0].encode())
            f.write('\n'.encode())
        print('保存信息成功')

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)



def getlist2(url):
    # 获取列表URL
    try:
        global j3
        j3 += 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('第%s轮，第3次·网络状态码: '%j3,res.status_code)
        #print(res.content.decode('utf-8'))
        pattern = re.compile('<li logr="(.*?)  </li>', re.S)  # <img class="" src=
        result = pattern.findall(res.text)
        # print(result)
        for url in result:
            pattern = re.compile('href="(.*?)"\n', re.S)  # <img class="" src=
            url = pattern.findall(url)
            #print(url[0])
            urllist2.append(url[0])
        print(urllist2)
        print(len(urllist2))

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


def getmessage2(url):
    # 获取列表URL
    try:
        global j4
        j4 += 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('第%s轮，第4次·网络状态码: '%j4,res.status_code)
        #print(res.content.decode('utf-8'))
        path=r'E:\信息'
        if  not os.path.exists(path):
            os.makedirs(path)
        filename = path + '/' + '仓库2' + '.txt'
        with open(filename, 'ab') as f:
            print('准备保存信息片段·')
            pattern = re.compile('<h1 class="c_000 f20">\(出租\)&nbsp;(.*?)</h1>', re.S)  # 海沧东浮镇50000平标准物流仓库出租滴水12米双边库
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  。  '.encode())
            pattern = re.compile(
                ' <span class="title">区&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;域：</span>\n                    (.*?)                </p>',
                re.S)  # 海沧
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="address">(.*?)</span>', re.S)  # 海沧东孚
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="up">(\d*?)m²</span>', re.S)  # 5000m²
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="house_basic_title_money_num_second">(.*?)元/m²/天&nbsp;&nbsp;&nbsp;&nbsp;',
                                 re.S)  # 0.9
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="house_basic_title_money_num">(.*?)</span>', re.S)  # 135
            result = pattern.findall(res.text)
            print(result)
            f.write(result[0].encode())
            f.write('  ，  '.encode())
            pattern = re.compile('<span class="house_basic_title_money_unit">(.*?)</span>', re.S)  # 单位
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                f.write(result[0].encode())
            f.write('\n'.encode())
        print('保存信息成功')

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == "__main__":

    for i in range(1,2):
        url = 'http://xm.ganji.com/cangkucf/b1/pn%s/?redundancy=seourl'%i#厂房
        getlist(url)
        time.sleep(2)
    for url in urllist[:3]:
        getmessage(url)
        time.sleep(2)

    for i in range(1,2):
        url = 'http://xm.ganji.com/changfang/b1/pn%s/?redundancy=seourl'%i#仓库
        getlist2(url)
        time.sleep(2)
    for url in urllist[:3]:
        getmessage2(url)
        time.sleep(2)