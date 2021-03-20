# -*-coding:  utf-8 -*-
# @Time    :  2021/3/5 17:02
# @Author  :  Cooper
# @FileName:  test2.py
# @Software:  PyCharm

import requests
import re
import csv
import random

i=0
url = "https://www.bilibili.com/v/popular/rank/bangumi?spm_id_from=333.851.b_62696c695f7265706f72745f616e696d65.51"
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36 QIHU 360SE"
}

def getlist(url):
    # 获取列表URL
    # try:
        global i
        res=requests.get(url, headers=header,timeout=20)
        print('第%s轮，第一次·网络状态码: '%i,res.status_code)
        # print(res.text)
        # print(res.content.decode('utf-8'))
        pattern = re.compile('<div class="content">(.*?)</div></div>', re.S)  # <img class="" src=
        result = pattern.findall(res.text)
        # print(result)


        with open(r"text2.csv", 'w', encoding='UTF-8-sig', newline='') as f:
            w = csv.writer(f)
            a=['排名', '番剧名称', '更新至第几话', '播放量/万', '弹幕数量/万', '追番人数/万', '综合得分', '均集播放/万', '均集活跃/万']
            w.writerow(a)
            for item in result:
                lis=[]
                print(item)
                # a=['第1名', '关于我转生变成史莱姆这档事 第二季', '更新至第32话', '播放量：1亿', '弹幕数量：66.1万', '追番人数：783.2万', '综合得分：2820983']
                # print(type(a))
                # w.writerow(a)
                i+=1
                lis.append('第%s名'%i)
                pattern = re.compile('target="_blank" class="title">(.*?)</a>', re.S)  # 番剧名称
                result = pattern.findall(item)
                lis.append(result[0])
                #更新到第几级
                pattern = re.compile('<div class="pgc-info">[\u4e00-\u9fa5]*(.*?)[\u4e00-\u9fa5]*</div>', re.S)  # 把汉字去除
                # pattern = re.compile('<div class="pgc-info">(.*?)</div>', re.S)  # 原来的
                result = pattern.findall(item)
                print('result[0]======',result[0])
                if result[0] == '':
                    lis.append(1)
                else:
                    print(result[0])
                    lis.append(result[0])
                pattern = re.compile('<i class="b-icon play"></i>\s*(.*?)(万|亿)', re.S)  # 播放量
                result = pattern.findall(item)
                print(result)
                print(result[0][1])

                if '亿' in result[0][1]:
                    print('ok')
                    lis.append(10000*float(result[0][0]))
                else:
                    lis.append(result[0][0])

                pattern = re.compile('span class="data-box"><i class="b-icon view"></i>\s*(.*?)(万|\n)', re.S)  # 弹幕数量
                result = pattern.findall(item)
                print(result[0][1])
                if '万' in result[0][1]:
                    lis.append(result[0][0])
                else:
                    lis.append(float(result[0][0])/10000)
                pattern = re.compile('</span> <span class="data-box"><i class="fav"></i>\s*(.*?)万', re.S)  #追番人数
                result = pattern.findall(item)
                lis.append(result[0])
                pattern = re.compile('<div class="pts"><div>(.*?)</div>综合得分', re.S)  # 综合得分
                result = pattern.findall(item)
                lis.append(result[0])

                # print(type(lis))
                # print(lis)bar.render("E:地区鞋价格.html") #这里我指定了我的存放路径和文件名
                # print('(lis[3])',(lis[3]))
                # print('(lis[2])',(lis[2]))
                print(float(lis[3]) / float(lis[2]))
                lis.append(int(float(lis[3]) / float(lis[2])))
                lis.append(round((float(lis[4]) / float(lis[2])),2))
                w.writerows([lis])#注意这里#写入多行
                print(lis)

if __name__ == "__main__":
    getlist(url)