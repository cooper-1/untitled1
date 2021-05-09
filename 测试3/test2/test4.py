# -*-coding:  utf-8 -*-
# @Time    :  2021/3/7 22:46
# @Author  :  Cooper
# @FileName:  test4.py
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
# response = requests.get("https://www.pixiv.net/", headers=headers)
response = requests.get("https://www.vmgirls.com/12973.html", headers=headers)
html = response.text
# print(html)
#利用正则表达式分析网页
#https://static.vmgirls.com/image/2019/10/AC084603-6289-40AD-B100-2DC90500E420.jpeg
dir_name = re.findall('<h1 class="post-title h1">(.*)</h1>', html)[-1]
print('dir_name',dir_name)
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# else:
#     print("文件查找失败！")
pattern = re.compile('style="background-image:url\(\'(.*?)\'', re.S)  # class="preview" href=
result = pattern.findall(html)
print(result)
a='https://static.vmgirls.com/image/2019/10/B1F023A6-A068-4B6F-ACD7-8A79D597A24F.jpeg '
print(a in result)
for url in set(result[:-1]):
    url='https:'+url
#保存数据
    print('url',url)
    time.sleep(1)
    i=i+1
    file_name = str(i)+'.jpg'
    print('第%s次准备保存图片·' % i, url)
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(requests.get(url, headers=headers, timeout=10).content)
        #https://static.vmgirls.com/image/2019/10/B1F023A6-A068-4B6F-ACD7-8A79D597A24F.jpeg
        #https://static.vmgirls.com/image/2019/10/B1F023A6-A068-4B6F-ACD7-8A79D597A24F.jpeg
