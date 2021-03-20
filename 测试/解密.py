# -*-coding:  utf-8 -*-
# @Time    :  2021/2/4 21:26
# @Author  :  Cooper
# @FileName:  解密.py
# @Software:  PyCharm
from Crypto.Cipher import AES
import os
import requests

keyurl='https://www.fhbf9.com/20210110/8raDl2kj/800kb/hls/key.key'
path = 'E:\视频\加密电影'
filename ='E:\视频\加密电影\IUz6flj9.ts'
filename ='E:\视频\加密电影\IUz6flj911.ts'
# ______________________
key = requests.get(keyurl).content
cryptor = AES.new(key, AES.MODE_CBC, key)  # 通过AES对ts进行解密
# ______________________
with open('E:\视频\加密电影\IUz6flj9.ts', 'rb') as f:
    with open('E:\视频\加密电影\IUz6flj911.ts', 'wb') as f1:
        f1.write(cryptor.decrypt(f.read()))