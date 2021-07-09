# -*-coding:  UTF-8
# @Time    :  2021/6/4 23:24
# @Author  :  Cooper
# @FileName:  爬取全国城市.py
# @Software:  PyCharm

import requests
import random
from requests.exceptions import ReadTimeout, HTTPError, RequestException
from lxml import etree
import agency.proxies

user_agent_list = agency.proxies.user_agent_list

i = 0


def getlist(url):
    # 获取列表URL
    try:
        global i
        i = i + 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=10)
        print('第%s轮，第一次·网络状态码： ' % i, res.status_code)
        # print(res.content.decode('utf-8'))
        html = etree.HTML(res.content.decode('utf-8'))
        infor = html.xpath('//div[@class="bottom"]/ul/li/a/text()')
        print('\n'.join(x.strip() for x in infor))
        citys = html.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()')
        print(citys)
        print(len(citys))
        citys = html.xpath('//div[@class="bottom"]/ul//li/a/text()')
        print(len(citys))
        citys = html.xpath('//div[@class="bottom"]/ul/li/a/text()|//div[@class="bottom"]/ul/div[2]/li/a/text()')
        print(len(citys))

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    getlist('https://www.aqistudy.cn/historydata/')
