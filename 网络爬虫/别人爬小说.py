from pyquery import PyQuery as pq
import requests


#输入保存到本地的文件名
filename = input("Please input the name you want to save: ")
#提供小说的编号，https://www.biqukan.com/0_790/   提供0_790就行，输入0_790
book_url = input("Please input url of this novel: ")

#获取小说文本内容
def get_txt(url):
    #获取url的返回值
    response = requests.get(url)
    #获取网页内容
    tmp_title = pq(response.text)
    #通过pyquery的特性，直接取页面中的h1标签文本内容，这个就是小说当前章节标题
    title = tmp_title("h1").text()
    #获取小说内容，#content，是通过id名取值，  .是通过类名，这里是通过id名，获取content的文本内容，当前章节的内容
    content = tmp_title("#content").text()
    #返回标题然后换行后内容
    return title + "\n" + content

#定义download函数
def download(url):
    #打开文件，编码为utf-8，别名叫file
    with open(filename,"a+",encoding="utf-8") as file:
        #调用get_txt这个函数，并且把download函数接收到的url传给get_txt函数，然后把返回的小说标题和内容写入到文件中
        file.write(get_txt(url))
        #写入两个回车，这样能看出一章是一章
        file.write("\n\n")

#定义函数将每一章小说都写入到文件中
def input_file(book_name):
    #拼接url
    split = "https://www.biqukan.com/" + book_name
    #h获取页面
    a = requests.get(split)
    #获取网页内容
    b = pq(a.text)
    #获取.listmain类的a标签，就是下一章的连接
    links = b(".listmain a")
    #循环所有的下一章
    for i in links[12:]:
        #调用download函数，拼接每一章的连接
        download("https://www.biqukan.com" + i.items()[0][1])

#输出下载中
print("downloading......please wait...")
#调用input_file函数，并且把小说编号当做参数传过去
input_file(book_url)
#输出下载完成
print("download is done....")

