# -*-coding:  UTF-8
# @Time    :  2021/6/2 23:11
# @Author  :  Cooper
# @FileName:  58同城.py
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
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=10)
        print('第%s轮，第一次·网络状态码： ' % i, res.status_code)
        # print(res.content.decode('utf-8'))
        html = etree.HTML(res.content.decode('utf-8'))
        infor = html.xpath('//ul[@class="house-list"]/li/div[2]/h2/a/text()')
        print('\n'.join(x.strip() for x in infor))



    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    getlist(
        'https://gz.58.com/chuzu/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0000-30ab-1b15-0079cbbea8be&ClickID=2')
