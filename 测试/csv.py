# -*-coding:  utf-8 -*-
# @Time    :  2021/2/10 1:37
# @Author  :  Cooper
# @FileName:  text12.py
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
    # ????????????URL
    try:
        global j
        j += 1
        header = {'User-Agent': random.choice(user_agent_list)}  # ???????????????user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('???%s????????????????????????????????: '%j,res.status_code)
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
    # ????????????URL
    try:
        global j2
        j2+=1
        message=[]
        header = {'User-Agent': random.choice(user_agent_list)}  # ???????????????user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('???%s????????????????????????????????: '%j2,res.status_code)
        #print(res.content.decode('utf-8'))
        path=r'E:\??????'
        if  not os.path.exists(path):
            os.makedirs(path)
        filename = path + '/' + '?????????3' + '.csv'
        with open(filename, 'a+', encoding='UTF-8', newline='') as f:
            w = csv.writer(f)
            print('??????????????????????????')
            pattern = re.compile('<h1 class="c_000 f20">\(??????\)&nbsp;(.*?)</h1>', re.S)  # ???????????????50000?????????????????????????????????12????????????
            result = pattern.findall(res.text)
            print(result)
            message.append(result[0])
            pattern = re.compile(
                ' <span class="title">???&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;??????</span>\n                    (.*?)                </p>',
                re.S)  # ??????
            result = pattern.findall(res.text)
            print(result)
            message.append(result[0])
            pattern = re.compile('<span class="address">(.*?)</span>', re.S)  # ????????????
            result = pattern.findall(res.text)
            print(result)
            message.append(result[0])
            pattern = re.compile('<span class="up">(\d*?)m??</span>', re.S)  # 5000m??
            result = pattern.findall(res.text)
            print(result)
            message.append(result[0])
            pattern = re.compile(
                '<span class="house_basic_title_money_num_second">(.*?)&nbsp;&nbsp;&nbsp;&nbsp;</span>', re.S)  # 0.9
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                message.append(result[0])
            else:
                message.append('???')

            pattern = re.compile('<span class="house_basic_title_money_num">(.*?)</span>', re.S)  # 135
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                message.append(result[0])  # ???
            else:
                message.append('???')
            pattern = re.compile('<span class="house_basic_title_money_unit">(.*?)</span>', re.S)  # ??????
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                message.append(result[0])  # ???
            else:
                message.append('???')
            w.writerow(message)  # ???
        print(message)

        print('??????????????????')

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)



def getlist2(url):
    # ????????????URL
    try:
        global j3
        j3 += 1
        header = {'User-Agent': random.choice(user_agent_list)}  # ???????????????user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('???%s?????????3????????????????????: '%j3,res.status_code)
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
    # ????????????URL
    try:
        global j4
        j4 += 1
        message=[]
        header = {'User-Agent': random.choice(user_agent_list)}  # ???????????????user-agent
        #proxy ={'http': 'http://59.29.245.151:3128'}
        res=requests.get(url, headers=header,  verify=False,timeout=20)
        print('???%s?????????4????????????????????: '%j4,res.status_code)
        #print(res.content.decode('utf-8'))
        path=r'E:\??????'
        if  not os.path.exists(path):
            os.makedirs(path)
        filename = path + '/' + '?????????4' + '.csv'
        with open(filename, 'a+',encoding='UTF-8',newline='') as f:
            w=csv.writer(f)
            print('??????????????????????????')
            pattern = re.compile('<h1 class="c_000 f20">\(??????\)&nbsp;(.*?)</h1>', re.S)  # ???????????????50000?????????????????????????????????12????????????
            result = pattern.findall(res.text)
            print(result)
            message.append(result[0])
            pattern = re.compile(
                ' <span class="title">???&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;??????</span>\n                    (.*?)                </p>',
                re.S)  # ??????
            result = pattern.findall(res.text)
            print(result)
            message.append(result[0])
            pattern = re.compile('<span class="address">(.*?)</span>', re.S)  # ????????????
            result = pattern.findall(res.text)
            print(result)
            message.append(result[0])
            pattern = re.compile('<span class="up">(\d*?)m??</span>', re.S)  # 5000m??
            result = pattern.findall(res.text)
            print(result)
            message.append(result[0])
            pattern = re.compile(
                '<span class="house_basic_title_money_num_second">(.*?)&nbsp;&nbsp;&nbsp;&nbsp;</span>', re.S)  # 0.9
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                message.append(result[0])
            else:
                message.append('???')

            pattern = re.compile('<span class="house_basic_title_money_num">(.*?)</span>', re.S)  # 135
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                message.append(result[0])
            else:
                message.append('???')
            pattern = re.compile('<span class="house_basic_title_money_unit">(.*?)</span>', re.S)  # ??????
            result = pattern.findall(res.text)
            if (len(result) != 0):
                print(result)
                message.append(result[0])#???
            else:
                message.append('???')
            w.writerow(message)  # ???
        print(message)

        print('??????????????????')

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == "__main__":

    for i in range(1,21):
        url = 'http://xm.ganji.com/cangkucf/b1/pn%s/?redundancy=seourl'%i#??????20
        getlist(url)
        time.sleep(3)
    for url in urllist:
        getmessage(url)#638
        time.sleep(3)

    for i in range(1,20):
        url = 'http://xm.ganji.com/changfang/b1/pn%s/?redundancy=seourl'%i#??????21
        getlist2(url)
        time.sleep(3)
    for url in urllist2:
        getmessage2(url)
        time.sleep(3)