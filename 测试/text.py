# -*-coding:  utf-8 -*-
# @Time    :  2020/12/18 12:26
# @Author  :  Cooper
# @FileName:  text.py
# @Software:  PyCharm
import re
import json
import requests
list=['https://th.wallhaven.cc/small/3z/3zkqp6.jpg', 'https://th.wallhaven.cc/small/vm/vmdov5.jpg', 'https://th.wallhaven.cc/small/73/73zpr3.jpg', 'https://th.wallhaven.cc/small/96/965kww.jpg', 'https://th.wallhaven.cc/small/83/83yx61.jpg', 'https://th.wallhaven.cc/small/lm/lmek62.jpg', 'https://th.wallhaven.cc/small/g8/g8rmme.jpg', 'https://th.wallhaven.cc/small/ym/ym67dg.jpg', 'https://th.wallhaven.cc/small/vm/vmyr3m.jpg', 'https://th.wallhaven.cc/small/od/odl8ml.jpg', 'https://th.wallhaven.cc/small/zm/zm1w2g.jpg']
url='https:\/\/p0.ssl.qhimgs1.com\/t0165ab238eedf25f1a.gif'
r='\\'
url=url.replace(r,'/')
print(url)
requests.get(url, timeout=10)
