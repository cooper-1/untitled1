# -*-coding:  utf-8 -*-
# @Time    :  2021/3/8 22:58
# @Author  :  Cooper
# @FileName:  test7.py
# @Software:  PyCharm
# _*_ coding=utf-8 _*_

import time
import re
import os
import requests

i=0
#拿到了网页源代码
headers = {
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome / 84.0.4147.89Safari / 53,,7.36 SLBrowser / 7.0.0.1071SLBChan / 30"
}
response = requests.get("https://www.vmgirls.com/12973.html", headers=headers)
html = response.text
# print(html)
#利用正则表达式分析网页
dir_name = re.findall('<h1 class="post-title h1">(.*)</h1>', html)[-1]
# print(dir_name)
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# else:
#     print("文件查找失败！")
urls = re.findall('<img alt="再见了夏天-唯美女生" .*?data-pagespeed-lsc-url="(.*?)">', html)
urls = str(urls)
url = re.sub("alt=\"再见了夏天\" title=\"再见了夏天'", "", urls)
# a = url.split('>')[0]
u = re.sub("/></a> <a href=\"(.*?)\"", "", url)
print(u)

print(u.split(','))
#保存数据
for a in u.split(','):
    # time.sleep(1)
    # print(type(a))

    url=re.sub(r'[\' "\[\]]','',a)
    print(url)
    print(type(url))
    #https://static.vmgirls.com/image/2019/10/006028D4-42B1-4FC5-A26F-FDBB19DDC9B8.jpeg
    #https://static.vmgirls.com/image/2019/10/006028D4-42B1-4FC5-A26F-FDBB19DDC9B8.jpeg
    # i = i + 1
    d = url.split('.')[-1]
    # filename = dir_name + '/' + str(i) +'12.'+ str(d)
    # url=' https://static.vmgirls.com/image/2019/10/006028D4-42B1-4FC5-A26F-FDBB19DDC9B8.jpeg'
    # url=re.sub(r'@[a-z]+','',url)
    # print(url in re.sub(r'[\'"\[\]]', '', a) )

    time.sleep(1)
    i = i + 1
    file_name = str(i) + '5.jpg'
    print('第%s次准备保存图片·' % i, url)
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(requests.get(url, headers=headers, timeout=10).content)
    # file_name = a.split('/')[-1]
    # response = requests.get(a, headers=headers)
    # with open(dir_name + '/' + file_name, 'wb') as f:
    #     f.write(response.content)