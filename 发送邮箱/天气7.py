# -*-coding:  UTF-8
# @Time    :  2021/5/15 23:36
# @Author  :  Cooper
# @FileName:  天气7.py

import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
import re
import random
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import schedule
import time

i = 0
j = 0
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
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]


def getlist(url):
    # 获取列表URL
    try:
        global i
        i = i + 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=20)
        print('第%s轮，第一次·网络状态码: ' % i, res.status_code, url)
        # print(res.content.decode('utf-8'))
        # pattern = re.compile('<ul class="clearfix">(.*?)<div class="slid">', re.S)  # <img class="" src=
        pattern = re.compile('<ul class="t clearfix">(.*?)</ul>', re.S)  # <img class="" src=
        result = pattern.findall(res.content.decode('utf-8'))
        print(result)
        print(len(result))
        print(result[0])
        sendmail('<ul class="t clearfix">' + result[0] + '</ul>')

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)
        getlist1()
        getlist()

def sendmail(result):
    # 请自行修改下面的邮件发送者和接收者
    sender = "yx1274814498@163.com"  # 发送方地址
    receivers = ['yx1274814498@163.com', '1274814498@qq.com', '1506262492@qq.com', '1651122140@qq.com',
                 '770031105@qq.com', '1593809016@qq.com']  # "1274814498@qq.com,770031105@qq.com,yx1274814498@163.com"
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = "yx1274814498@163.com"
    message['To'] = 'yx1274814498@163.com,770031105@qq.com,1274814498@qq.com'
    message['Subject'] = Header('1274814498@qq.com示例代码实验邮件', 'utf-8')
    # smtper = SMTP('smtp.163.com',465)
    smtper = smtplib.SMTP_SSL()
    smtper = smtplib.SMTP_SSL('smtp.163.com', 465)
    message = MIMEMultipart('related')
    message['Subject'] = '闰京的 message'

    msgText = MIMEText(result + '<br><img src="cid:image1"><br>', 'html', 'utf-8')

    message.attach(msgText)

    fp = open(r'img.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)

    # 请自行修改下面的登录口令
    smtper.ehlo()
    # smtper.starttls()
    smtper.login(sender, "SBMMBSAHCMPDUOWC")  # 此处secretpass输入授权码
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')
    smtper.quit()


def getlist1( url = 'https://search.bilibili.com/article?keyword=p%E7%AB%99'):
    # 获取列表URL
    try:
        global j
        j=j+1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res=requests.get(url, headers=header,timeout=20)
        print('准备下载图片·第%s轮·第一次网络状态码: '%j,res.status_code)
        # print(res.content.decode('utf-8'))
        pattern = re.compile('<li class="article-item"><a href="(.*?)" title=', re.S)  # <img class="" src=
        result = pattern.findall(res.content.decode('utf-8'))
        # print(result)
        print(random.choice(result))
        url=(random.choice(result))
        url='https:'+url
        print('url==',url)
        getlist2(url)

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


def  getlist2(url):
    global i
    header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
    res = requests.get(url, headers=header, timeout=10)
    print('下载图片·第%s轮·第二网络状态码：' % i, res.status_code)
    pattern = re.compile('img data-src="(.*?)"', re.S)  # class="preview" href=
    result = pattern.findall(res.text)
    print('result===', result)
    list2 = []
    for url in result:
        list2.append('https:' + url)
    print(list2)
    print(random.choice(list2))
    url =random.choice(list2)
    i = i + 1
    filename ='img.jpg'
    print('第%s次准备保存图片·' % i, url)
    with open(filename, 'wb') as f:
        f.write(requests.get(url, headers=header, timeout=10).content)

if __name__ == "__main__":
    schedule.every().day.at("07:25").do(getlist1)
    # getlist1()
    # schedule.every(5).seconds.do(getlist1)
    # url = 'http://www.weather.com.cn/weather/101280201.shtml'韶关
    # url = 'http://www.weather.com.cn/weather1d/101281206.shtml#input'#河源东源
    url = 'http://www.weather.com.cn/weather/101281201.shtml'  # 河源
    schedule.every().day.at("07:30").do(getlist, url)
    getlist(url)
    # schedule.every(1).minutes.do(getlist,url)
    while True:
        schedule.run_pending()
        time.sleep(1)
