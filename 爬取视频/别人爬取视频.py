import requests
import csv
import json

# import pprint

# 1分析目标网页 确定爬取的URL路径
page = 0
while True:
    page += 1
    print('=====================正在抓取第()页的数据=============='.format(page))
    url = 'https://api-tinyvideo-web.yy.com/home/tinyvideosv2'
    params = {
        'data':'{"uid":0,"page":%s,"pageSize":10}'%str(page)
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'

    }

    # 2发送请求 获得响应数据
    response = requests.get(url, headers=headers, params=params)

    #获取响应数据中的json数据
    data = response.json()
    # print(data)


    # 3解析数据
    # 提取字段
    data_list = data['data']['data']
    # print(data_list)

    ## 遍历列表
    for data in data_list:
        try:
            resdesc = data['resdesc'] +'.mp4'  #视频文件名

            resurl = data['resurl']   #视频的URL
            video_data = requests.get(url=resurl,headers=headers).content  #提取二进制数据
            with open('E:\\小说\\' + resdesc, mode='wb') as f:
                print('正在抓取视频', resdesc)
                f.write(video_data)
        except Exception as e:
            break




    # 4保存数据

    # 在项目下的文件夹新建一个文件夹保存视频



