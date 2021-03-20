# -*-coding:  utf-8 -*-
# @Time    :  2020/12/19 22:35
# @Author  :  Cooper
# @FileName:  网站爬图.py
# @Software:  PyCharm
# 导入必要的包
import requests
import os
import urllib


class Spider_baidu_image():
    def __init__(self):
        self.url = 'http://image.baidu.com/search/acjson?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.\
            3497.81 Safari/537.36'}
        self.headers_image = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.\
            3497.81 Safari/537.36',#Referer参照页，可以要也可以不用
            'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1557124645631_R&pv=&ic=&nc=1&z=&hd=1&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E8%83%A1%E6%AD%8C',
          }
        # self.keyword = '刘亦菲壁纸'
        self.keyword = input("请输入搜索图片关键字:")
        self.paginator = int(input("请输入搜索页数，每页30张图片："))
        # self.paginator = 50
        # print(type(self.keyword),self.paginator)
        # exit()

    def get_param(self):
        """
        获取url请求的参数，存入列表并返回
        :return:
        """
        keyword = urllib.parse.quote(self.keyword)#URL只容许一部分ASCII字符，其余字符（如汉字）是不符合标准的，此时就要进行编码。
        params = []
        for i in range(1, self.paginator + 1):
            params.append(
                'tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=1&latest=0&copyright=0&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=star&pn={}&rn=30&gsm=78&1557125391211='.format(
                    keyword, keyword, 30 * i))#一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。基本语法是通过 {} 和 : 来代替以前的 % """
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
            json_data = requests.get(url, headers=self.headers).json()#.json()处理过
            print(json_data)
            json_data = json_data.get('data')# get()方法语法：dict.get(key, default=None)key -- 字典中要查找的键。
            #[{adType: "0", hasAspData: "0",…}, {adType: "0", hasAspData: "0",…}, {adType: "0", hasAspData: "0",…},…]
            print(json_data)
            for i in json_data:
                print('i=======',i)
                if i:
                    image_url.append(i.get('thumbURL'))
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
    #spider()# 就等价于  spider.__call()__   这样的调用#  spider()  等于 spider.__call__()
    spider.__call__#  spider()  等于 spider.__call__()


