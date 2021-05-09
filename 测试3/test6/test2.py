# -*-coding:  utf-8
# @Time    :  2021/3/18 15:50
# @Author  :  Cooper
# @FileName:  test3.py
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import random
from selenium import webdriver
import time, re

j=0
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
def getlist(urls):
    try:   # 获取列表URL
        for url in urls:
            global j
            j += 1
            url='https://mxiaoyuan.zhaopin.com/App/Job?id='+url
            header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
            res=requests.get(url, headers=header,timeout=20)
            print('第%s轮，第一次·网络状态码: '%j,res.status_code,url)# print(res.content.decode('utf-8'))
            pattern = re.compile(r'<h4 class="jobName" id="h4JobTitle">(.*?)提醒：以担保或任何理由向求职者索取财物，扣押证照，均涉嫌违法。请您提高警惕。', re.S)
            result = pattern.findall(res.content.decode('utf-8'))
            pattern = re.compile(r'[\u4e00-\u9fa5]+', re.S)
            work = pattern.findall(result[0])
            print(work)
            with open(r"text3.txt", 'a+', encoding='UTF-8') as f:
                f.write(' '.join(work))
                f.write('\n')

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)

def get(url):
    options = webdriver.ChromeOptions()
    options.headless = True  # 设置选项为无界面
    options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)    # print(driver.page_source)
    pattern = re.compile(r'"JobPositionNumber":"(.*?)"', re.S)
    result = pattern.findall(driver.page_source)
    driver.quit()
    return result

if __name__ == '__main__':
    urls = ["https://xiaoyuan.zhaopin.com/search/jn=2&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&pg={}".format(x) for x in range(1, 35)]
    for url in urls[:10]:
        result=get(url)
        getlist(result)