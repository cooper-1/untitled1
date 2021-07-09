# -*-coding:  UTF-8
# @Time    :  2021/5/30 9:19
# @Author  :  Cooper
# @FileName:  post请求.py
# @Software:  PyCharm
import urllib.request
import urllib.parse
import jsonpath
import json

# url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# 新url增加了防爬参数，导致请求不成功，我们使用原有url就可以了
# url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

data = {
    'i': 'I love pythonn',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    # 'salt': '16223376911070',
    # 'sign': '5ea96ae9f20a7bd37262b454f5f28d9b',
    'lts': '1622337691107',
    'bv': ' b0ff5d17f404993192085bf8b1e93587',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': ' FY_BY_REALTlME'
}
# 对数据进行url编码
data = urllib.parse.urlencode(data)
# 转换为bytes对象
data = bytes(data.encode())
# 请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
# 构造request对象
request = urllib.request.Request(url, data=data, headers=header)
# 发送请求获取响应数据
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
# 把json字符串转换为python对象
store = json.loads(html)
# 打印响应结果
print(html)
# 查看store下tgt属性
jsonurl = '$..tgt'
result = jsonpath.jsonpath(store, jsonurl)
print(result[0])
