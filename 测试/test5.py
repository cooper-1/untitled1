# -*-coding:  utf-8 -*-
# @Time    :  2021/1/28 23:19
# @Author  :  Cooper
# @FileName:  test5.py
# @Software:  PyCharm
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
import time
import os
import re
import random
import agency.proxies
from agency.proxies import Proxy
proxylist=[
	{"http":"http://175.43.130.154:9999"},
	{"http":"http://183.166.20.129:9999"},
	{"http":"http://106.110.195.3:9999"},
	{"http":"http://175.44.108.75:9999"},
	{"http":"http://49.86.26.166:9999"},
	{"http":"http://113.121.37.248:9999"}
]
print(proxylist)
user_agent_list=agency.proxies.user_agent_list
proxylist=Proxy().getproxy()
print(user_agent_list)
print(len(proxylist))
