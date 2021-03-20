# -*-coding:  utf-8 -*-
# @Time    :  2020/12/20 16:14
# @Author  :  Cooper
# @FileName:  自写网爬搜狗图片.py
# @Software:  PyCharm

# 导入必要的包
import requests
import os
import urllib


class Spider_baidu_image():
    def __init__(self):
        self.url = 'https://image.so.com/j?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.\
            3497.81 Safari/537.36'}
        self.headers_image = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.\
            3497.81 Safari/537.36',#Referer参照页，可以要也可以不用
            #'Referer': 'https://image.so.com/i?q=%E9%87%91%E6%9C%A8&src=srp'
          }
        #self.keyword = '伊万卡'
        self.keyword = input("请输入搜索图片关键字:")
        #self.paginator = int(input("请输入搜索页数，每页60张图片："))
        self.paginator = 2


    def get_param(self):
        """
        获取url请求的参数，存入列表并返回
        :return:
        """
        keyword = urllib.parse.quote(self.keyword)#URL只容许一部分ASCII字符，其余字符（如汉字）是不符合标准的，此时就要进行编码。
        params = []
        for i in range(0, self.paginator + 1):
            j=111
            if i>0:
                j=60
            print(j)
            params.append(
                'q={}&pd=1&pn=60&correct={}&adstar=0&tab=all&sid=671bb036f4082959c769420d0a208bbe&ras=0&cn=0&gn=0&kn=50&crn=0&bxn=20&cuben=0&pornn=0&manun=50&src=srp&sn={}&ps={}&pc={}'.format(
                    keyword, keyword, (130+10 * i),(111+60*i),j))#一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。基本语法是通过 {} 和 : 来代替以前的 % """
        return params

    def get_urls(self, params):
        """
        由url参数返回各个url拼接后的响应，存入列表并返回
        :return:
        """
        urls = []
        for i in params:
            urls.append(self.url + i)
        return urls

    def get_image_url(self, urls):
        image_url = []
        for url in urls:
            json_data = requests.get(url, headers=self.headers)#.json()处理过
            print(json_data)
            json_data =json_data.json()#.json()处理过
            print(json_data)
            json_data = json_data.get('list')# get()方法语法：dict.get(key, default=None)key -- 字典中要查找的键。
            #[{adType: "0", hasAspData: "0",…}, {adType: "0", hasAspData: "0",…}, {adType: "0", hasAspData: "0",…},…]
            print(json_data)
            for i in json_data:
                print('i=======',i)
                if i:
                    image_url.append(i.get('thumb'))
        return image_url

    def get_image(self, image_url):
        """
        根据图片url，在本地目录下新建一个以搜索关键字命名的文件夹，然后将每一个图片存入。
        :param image_url:
        :return:
        """
        cwd = os.getcwd()#返回当前工作目录
        file_name = os.path.join(cwd, self.keyword)#将目录与文件名拼接起来
        print(file_name)
        if not os.path.exists(self.keyword):
            os.mkdir(file_name)#将文件夹名创建
        for index, url in enumerate(image_url, start=1):#seasons = ['Spring', 'Summer', 'Fall', 'Winter']  list(enumerate(seasons, start=1))       # 下标从 1 开始[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
            with open(file_name + '\\{}.jpg'.format(index), 'wb') as f:
                f.write(requests.get(url, headers=self.headers_image).content)#.content返回的是bytes字节码，数据库字段是image的类型为byte[]
            if index != 0 and index % 30 == 0:
                print('{}第{}页下载完成'.format(self.keyword, index / 30))

    def __call__(self, *args, **kwargs):
        '''只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。
         换句话说，我们可以把这个类型的对象当作函数来使用，相当于 重载了括号运算符。'''
        params = self.get_param()
        urls = self.get_urls(params)
        image_url = self.get_image_url(urls)
        self.get_image(image_url)


if __name__ == '__main__':
    spider = Spider_baidu_image()
    spider()


