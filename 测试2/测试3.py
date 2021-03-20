# -*-coding:  utf-8 -*-
# @Time    :  2021/3/4 21:59
# @Author  :  Cooper
# @FileName:  测试3.py
# @Software:  PyCharm
import urllib.request
import re
from bs4 import BeautifulSoup
import xlwt
url = "https://www.bilibili.com/v/popular/rank/bangumi?spm_id_from=333.851.b_62696c695f7265706f72745f616e696d65.51"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36 QIHU 360SE"
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode("utf-8")
print(html)

findImg = re.compile(r'<img .*src="(.*?)"')
findName = re.compile(r'<a .*target="_blank">(.*?)</a>')
findLink = re.compile(r'<a href="(.*?)"')
findPlay = re.compile(r'</i>(.*?)</span>', re.S)
findString = re.compile(r'<div>(.*?)</div>')

datalist = []
soup = BeautifulSoup(html, "html.parser")
for item in soup.find_all('div', class_="content"):
    data = []
    item = str(item)
    #番剧名称
    title = re.findall(findName, item)[0]
    data.append(title)
    #播放地址
    link = re.findall(findLink, item)[0]
    links = re.sub("//", "", link)
    data.append(links)
    #图片链接
    # tupian = re.findall(findImg, item)[0]
    # data.append(tupian)
     #播放量
    play = re.findall(findPlay, item)[0]
    plays = re.sub("\n( ){12,14}", "",play)
    data.append(plays)
    #弹幕数量
    danmu = re.findall(findPlay, item)[1]
    danmus = re.sub("\n( ){12,14}", "", danmu)
    data.append(danmus)
    #综合评分
    string = re.findall(findString, item)[0]
    data.append(string)

    print(data)
    datalist.append(data)

#写入excel
title = ["番剧名称","播放地址","播放量","弹幕数量","综合评分"]
book = xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet = book.add_sheet('bilibi排行榜',cell_overwrite_ok=True)
#添加
for i in range(len(title)):
    sheet.write(0, i, title[i])
for m in range(len(datalist)):
    for j in range(len(datalist[m])):
        sheet.write(m+1, j, datalist[m][j])

try:
    book.save("b站排行榜.xls")
    print("爬取成功！")
except Exception as a:
    print("保存失败！")