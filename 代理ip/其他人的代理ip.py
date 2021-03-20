import requests
import random
import agency.proxies
from agency.proxies import Proxy

url = 'https://www.baidu.com/'
user_agent_list=agency.proxies.user_agent_list
proxies_list = Proxy().getproxy()
ip_list = []
i=0
#print(proxies_list)
for proxy in proxies_list:
    print(proxy)
    # print(proxies_list)
    # proxies = proxy_ip
    try:
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, proxies=proxy, timeout=10)
        flag = True
    except:
        flag = False

    if flag:
        ip_list.append(proxy)
print(ip_list)