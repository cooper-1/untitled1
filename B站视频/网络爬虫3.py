# -*-coding:  utf-8 -*-
# @Time    :  2020/12/21 15:47
# @Author  :  Cooper
# @FileName:  网络爬虫3.py
# @Software:  PyCharm
import urllib.request as r
import urllib.parse as p
from pyquery import PyQuery as pq
import json
import os

# 打开url返回没有解码的html
def open_url(url):
    r.Request(url).add_header('User-Agent',
                              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36')
    respond = r.urlopen(url)
    try:
        if respond.getcode() == 200:
            html = respond.read()#返回的是html字符串类型
    except Exception as e:
        page = e.partial#可以用来"冻结"一个函数的参数，并返回"冻结"参数后的新函数
        html = page
    return html


# 获取初始化的图片（一般是页面前60或100张）
def find_imgurl(html):
    if html == None:
        return
    imgurl_dict = {}
    d = pq(html)  # 用爬回来的网页str进行网页分析
    scr = d('body')('script')('#initData')  # 找到对应的标签
    imgurl_dict = json_FindInitimg(scr.html(), imgurl_dict)
    return imgurl_dict


# 获取请求参数（获取请求参数）
def find_param(html):
    if html == None:
        return
    d = pq(html)  # 用爬回来的网页str进行网页分析
    scr = d('body')('script')('#initParam')  # 找到对应的标签
    param_dict = json.loads(scr.html().replace("'", '"'))           #爬取回来的参数字典
    return param_dict


# 通过参数形成新的url（通过这些参数形成新的url）
def Newurl(param_dict, num=1):
    urllist = []
    sn = 60
    ps = 1
    for i in range(num):
        URLdata = {
            'q': p.unquote(param_dict['query']),
            'pd': 1,
            'pn': 60,
            'correct': p.unquote(param_dict['query']),
            'adstar': param_dict['adstar'],
            'tab': param_dict['tab'],
            'sid': param_dict['sid'],
            'ras': param_dict['ras'],
            'cn': param_dict['cn'],
            'gn': param_dict['gn'],
            'kn': param_dict['kn'],
            'crn': param_dict['crn'],
            'bxn': param_dict['bxn'],
            'cuben': param_dict['cuben'],
            'src': 'srp',
            'sn': sn,
            'ps': ps,
            'pc': 60
        }
        url = 'https://image.so.com/j?' + p.urlencode(URLdata)
        print('生成批道url:   ' + url)
        urllist.append(url)
        sn += 70
        ps += 70
    return urllist


# 这里只是针对（页面前60-100张进行爬取）
def json_FindInitimg(string, imgurl_dict):
    js = json.loads(string)  # 将标签中的信息进行json加载
    for elevent in iter(js):
        if type(js[elevent]) == type([]):
            for lis in js[elevent]:
                for (key, value) in lis.items():
                    if key == 'thumb_bak':
                        print((key, value))
                        imgurl_dict[value] = value.split('/')[-1].split('.')[-1]
    return imgurl_dict


# 下载
def download(dirpath, imgurl_dict):
    count = 0
    print(imgurl_dict)
    for (imgurl, type) in imgurl_dict.items():
        if type == 'jpg' or type == 'png' or type == 'jpeg':
            print("图片[   %s   ]开始下载......" % imgurl)
            html = open_url(imgurl)
            path = dirpath + str(count) + '.' + type
            print("图片写入路径是:%s" % dirpath + path)
            with open(path, mode='wb') as f:
                f.write(html)
            count += 1
    return count


# 不同的下载方式，下载不同数量的图片
def download_img(url, dirpath, num=None):
    Pcount = 1  # 批道数

    if num == None:
        html = open_url(url).decode('utf-8')
        imgurl_dict = find_imgurl(html)
        os.mkdir(dirpath + str(Pcount))
        download(dirpath+str(Pcount)+'\\', imgurl_dict)
    else:
        html = open_url(url).decode('utf-8')

        for i in Newurl(find_param(html), num=num):
            newhtml = open_url(i).decode('utf-8')
            imgurl_dict = {}
            json_FindInitimg(newhtml, imgurl_dict)
            os.mkdir(dirpath+str(Pcount))        #工具批道数新建文件夹
            download(dirpath+str(Pcount)+'\\', imgurl_dict)          #下载到对应的文件夹
            Pcount +=1


if __name__ == '__main__':

    path =os.getcwd()      #根目录（每一批会在根目录建一个新目录）
    Qval = input('请输入你要搜索的图片：')
    mod = input('请输入爬取方式：（1:爬取页面前60-100张\t0:爬取指定数量）')
    data = {
        'q': Qval,
        'src': 'srp'
    }
    url = 'https://image.so.com/i?' + p.urlencode(data)#urlencode()函数原理就是首先把中文字符转换为十六进制，然后在每个字符前面加一个标识符%
    if mod == '1':
        download_img(url, dirpath=path)
    else:
        num = int(input('请输入爬取批数：（一般60/批）'))
        download_img(url, dirpath=path, num=num)

