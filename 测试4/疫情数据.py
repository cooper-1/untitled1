# -*-coding:  UTF-8
# @Time    :  2021/6/5 23:28
# @Author  :  Cooper
# @FileName:  疫情数据.py
# @Software:  PyCharm
import requests
import random
from requests.exceptions import ReadTimeout, HTTPError, RequestException
from lxml import etree
import agency.proxies
import re

user_agent_list = agency.proxies.user_agent_list

i = 0


def getlist3(url):
    # 获取列表URL
    try:
        global i
        i = i + 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=10)
        print('第%s轮，第一次·网络状态码： ' % i, res.status_code)
        # res.encoding = 'utf-8-sig'  # 注意要修改编码
        # print(res.content.decode('gbk'))

        pattern = re.compile('try { window.getTimelineService1 = (.*?)2021","infoSource":"央视新闻app",', re.S)  # 综合得分
        # pattern = re.compile('"pubDateStr":"14小时前","title":"(.*?)"infoSource"', re.S)  # 综合得分
        result = pattern.findall(res.content.decode('utf-8'))
        print(result[-1:])
        # with open('abc.txt', 'w',encoding='utf-8') as fp:
        #     fp.write(res.content.decode('utf-8'))

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # getlist('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4')
    getlist3('https://ncov.dxy.cn/ncovh5/view/pneumonia')