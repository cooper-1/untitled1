# -*-coding:  utf-8 -*-
# @Time    :  2021/2/4 11:59
# @Author  :  Cooper
# @FileName:  test9.py
# @Software:  PyCharm
import re
import requests
import m3u8
import time
import os
from bs4 import BeautifulSoup
import json
from Crypto.Cipher import AES


class VideoCrawler():
    def __init__(self, url):
        super(VideoCrawler, self).__init__()
        self.url = url
        self.down_path = r"F:\Media\Film\Temp"
        self.final_path = r"F:\Media\Film\Final"
        self.headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html,application/xhtml+xml,*/*',
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 6.0; zh-CN; MZ-m2 note Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 MZBrowser/6.5.506 UWS/2.10.1.22 Mobile Safari/537.36'
        }

    def get_url_from_m3u8(self, readAdr):
        print("正在解析真实下载地址...")
        with open('temp.m3u8', 'wb') as file:
            file.write(requests.get(readAdr).content)
        m3u8Obj = m3u8.load('temp.m3u8')
        print("解析完成")
        return m3u8Obj.segments

    def run(self):
        print("Start!")
        start_time = time.time()
        os.chdir(self.down_path)
        html = requests.get(self.url).text
        bsObj = BeautifulSoup(html, 'lxml')
        tempStr = bsObj.find(class_="iplays").contents[3].string  # 通过class查找存放m3u8地址的组件
        firstM3u8Adr = json.loads(tempStr.strip('var player_data='))["url"]  # 得到第一层m3u8地址
        tempArr = firstM3u8Adr.rpartition('/')
        realAdr = "%s/500kb/hls/%s" % (tempArr[0], tempArr[2])  # 一定规律下对字符串拼接得到第二层地址， 得到真实m3u8下载地址，
        key_url = "%s/500kb/hls/key.key" % tempArr[0]  # 分析规律对字符串拼接得到key的地址
        key = requests.get(key_url).content
        fileName = bsObj.find(class_="video-title w100").contents[0].contents[0]  # 从源码中找到视频名称的规律
        fileName = re.sub(r'[\s,!]', '', fileName)  # 通过正则表达式去掉中文名称中的感叹号逗号和空格等特殊字符串
        cryptor = AES.new(key, AES.MODE_CBC, key)  # 通过AES对ts进行解密
        urlList = self.get_url_from_m3u8(realAdr)
        urlRoot = tempArr[0]
        i = 1
        for url in urlList:
            resp = requests.get("%s/500kb/hls/%s" % (urlRoot, url.uri), headers=crawler.headers)
            if len(key):
                with open('clip%s.ts' % i, 'wb') as f:
                    f.write(cryptor.decrypt(resp.content))
                    print("正在下载clip%d" % i)
            else:
                with open('clip%s.ts' % i, 'wb') as f:
                    f.write(resp.content)
                    print("正在下载clip%d" % i)
            i += 1
        print("下载完成！总共耗时%d s" % (time.time() - start_time))
        print("接下来进行合并......")
        os.system('copy/b %s\\*.ts %s\\%s.ts' % (self.down_path, self.final_path, fileName))
        print("删除碎片源文件......")
        files = os.listdir(self.down_path)
        for filena in files:
            del_file = self.down_path + '\\' + filena
            os.remove(del_file)
        print("碎片文件删除完成")


if __name__ == '__main__':
    crawler = VideoCrawler("地址大家自己找哦")
    crawler.start()
    crawler2 = VideoCrawler("地址大家自己找哦")
    crawler2.start()