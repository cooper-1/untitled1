# -*-coding:  utf-8 -*-
# @Time    :  2020/12/18 13:56
# @Author  :  Cooper
# @FileName:  爬虫36.py
# @Software:  PyCharm
import requests,re
import time
from requests.exceptions import ReadTimeout,HTTPError,RequestException
from bs4 import BeautifulSoup

url='https://movie.douban.com/top250?start='

key_dict={'key1':'value1','key2':'value2'}
headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
         'Host':'movie.douban.com'}
proxy={'http':'175.155.141.242 :1133'}
movie_list=[]

for i in range(0,10):
    #time.sleep(2)
    url = 'https://movie.douban.com/top250?start='+str(i*25)
    response=requests.get(url,params=key_dict,headers=headers,timeout=30)
    print('第 '+str(i+1)+' 页响应状态码：',response.status_code)
    soup = BeautifulSoup(response.text,"lxml")
    div_list=soup.find_all('div',class_='hd')# 查找所有class属性为hd的div标签
    for each in div_list :
        print(each)
        # 获取每个div中的a中的span（第一个），并获取其文本
        movie=each.a.span.text.strip()#strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        # #注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
        movie_list.append(movie)
        filename = 'quotes-%s.txt' % i
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(movie + '\n')

print(movie_list)