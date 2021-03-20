# -*-coding:  utf-8 -*-
# @Time    :  2021/3/14 23:05
# @Author  :  Cooper
# @FileName:  test13.py
# @Software:  PyCharm
import re
import os
import requests

#拿到了网页源代码
headers = {
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome / 84.0.4147.89Safari / 53,,7.36 SLBrowser / 7.0.0.1071SLBChan / 30"
}

baseurl = "https://www.enterdesk.com/zt/pvp/"                      #远坂凛 "https://www.sohu.com/a/310941387_539420?sec=wd"
response = requests.get(baseurl, headers=headers)
html = response.text
print(html)
#利用正则表达式分析网页
dir_name = re.findall(r'<meta name="keywords" content="(.*?)">', html, re.S)[-1]
print(dir_name)
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
else:
    pass

urls = re.findall(r'src="(.*?)\.jpg', html,re.S)
print(urls)

for url in urls:
    url=url+'.jpg'
    file_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    with open(dir_name + '/' + file_name, 'wb') as f:
        f.write(response.content)
