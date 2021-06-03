# -*-coding:  UTF-8
# @Time    :  2021/6/3 23:52
# @Author  :  Cooper
# @FileName:  4k图片网.py
# @Software:  PyCharm
import requests
import random
import os
from requests.exceptions import ReadTimeout, HTTPError, RequestException
from lxml import etree
import agency.proxies
user_agent_list = agency.proxies.user_agent_list
ii = 0
j = 0

def getlist(url):
    # 获取列表URL
    try:
        global j
        j = j + 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=10)
        print('第%s轮 · 第一次·网络状态码： ' % j, res.status_code)
        # print(res.content.decode('utf-8'))
        html = etree.HTML(res.content)
        infor = html.xpath('//ul[@class="clearfix"]/li/a/img/@src')
        # print('\n'.join(x.strip() for x in infor))
        name = html.xpath('//ul[@class="clearfix"]/li/a/b/text()')
        # print('\n'.join(x.strip() for x in name))
        dic = dict(zip(infor, name))
        print(dic)
        path = r'E:\B站\图片29'
        if not os.path.exists(path):
            os.makedirs(path)
            print('目录创建成功！')
        else:
            print('该目录已经存在')
        for url, name in dic.items():
            global ii
            # print(url, name)
            ii = ii + 1
            filename = path + '/' + name + '.jpg'
            with open(filename, 'wb') as f:
                f.write(requests.get('https://pic.netbian.com' + url, headers=header, timeout=20).content)
            print('第 %s 张图片保存成功' % ii, name, 'https://pic.netbian.com' + url)

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for i in range(1, 10):
        url = 'https://pic.netbian.com/e/search/result/index.php?page={}&searchid=1869'.format(i)
        getlist(url)
