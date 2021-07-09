# -*-coding:  UTF-8
# @Time    :  2021/6/20 14:39
# @Author  :  Cooper
# @FileName:  识别古诗文网.py
# @Software:  PyCharm
import requests
from lxml import etree
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
import re
import time
import random
# 导入自定义的包
from agency import chaojiying

# 2.考虑session
#   可能会产生session的请求都用session发起
session = requests.Session()
j = 0
i = 0
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


# 使用超级鹰云打码平台的使用流程
# 第一将识别的验证码下载到本地保存
def getlist(url):
    # 获取列表URL
    try:
        global j, i
        j += 1
        i += 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=20)
        print('第%s轮，第一次·网络状态码: ' % j, res.status_code)
        # print(res.content.decode('utf-8'))
        # 解析页面中验证码图片img中src的属性值
        tree = etree.HTML(res.content.decode('utf-8'))
        imgsrc = 'https://so.gushiwen.cn/' + tree.xpath('//img[@id="imgCode"]/@src')[0]
        # 获取动态变化的请求值
        __VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
        __VIEWSTATEGENERATOR = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]

        print(imgsrc)
        print('准备保存图片·')
        filename = 'img.jpg'
        print(__VIEWSTATE)
        print(__VIEWSTATEGENERATOR)
        with open(filename, 'wb') as f:
            f.write(requests.get(imgsrc).content)
        print('第%s张图片保存成功' % i, url)
        yzm = recognition(filename)
        login(yzm, __VIEWSTATE, __VIEWSTATEGENERATOR)

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


# 第二调用云平台的接口识别验证码
def recognition(filename):
    chaojiying2 = chaojiying.Chaojiying_Client('18819776051', '1274814498.qq', '918466')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(filename, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    mess = chaojiying2.PostPic(im, 1902)
    print(mess['pic_str'])  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    return mess['pic_str']


def login(code_text, __VIEWSTATE, __VIEWSTATEGENERATOR):
    # 获取列表URL
    try:
        global j, i
        j += 1
        i += 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        # 模拟登录
        data = {
            '__VIEWSTATE': __VIEWSTATE,
            '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
            'from': 'http://so.gushiwen.cn/user/collect.aspx',
            'email': '1274814498@qq.com',
            'pwd': '18819776051',
            'code': code_text,
            'denglu': '登录',
        }
        # 考虑1：动态变化的请求参数
        #   通常会隐藏在当前对应的前端页面的代码中

        login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
        page_index = session.post(url=login_url, headers=header, data=data).text
        # print(page_index)
        with open('index.html', 'w', encoding='utf-8') as fp:
            fp.write(page_index)

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    getlist(url)
