# -*-coding:  UTF-8
# @Time    :  2021/6/5 23:56
# @Author  :  Cooper
# @FileName:  爬取疫情2.py
# @Software:  PyCharm
import  requests
from  bs4 import BeautifulSoup
import re
import json

# 1.发送请求，获取疫情首页（数据来源于丁香园）
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()

# 2.从疫情首页提取最近一日数据
soup = BeautifulSoup(home_page, 'lxml')
script = soup.find(id='getAreaStat')
text = script.string

# 3.提取数据获取json格式数据
json_str = re.findall(r'\[.+\]', text)[0]

# 4.把json格式转换为python类型
last_day_corona_virus = json.loads(json_str)

# 5.以json格式保存最近一日数据
with open('oronavirus.json', 'w') as fp:
    json.dump(last_day_corona_virus, fp, ensure_ascii=False)
