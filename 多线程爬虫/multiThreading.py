import threading #使用线程库
import time
from queue import Queue #队列
from lxml import etree #解析库
import requests #请求处理
import json #json处理

class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        threading.Thread.__init__(self)
        # super(ThreadCrawl,self).__init__()
        self.threadName = threadName #线程名
        self.pageQueue = pageQueue #页码队列
        self.dataQueue = dataQueue #数据队列
        #请求报头
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                    'Accept-Language': 'zh-CN,zh;q=0.8'}
        #  '{"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}'


    def run(self):
        print("启动 "+self.threadName)
        while not CRAWL_EXIT:
            try:
                ##从dataQueue中取出一个页码数字，先进先出
                #可选参数block,默认值是True
                #如果队列为空，block位True的话，不会结束，会进入阻塞状态，直到队列有新的数据
                #如果队列为空，block为False的话，就弹出一个Queue.empty()异常
                page = self.pageQueue.get(False)
                # 构建网页的URL地址
                url = "http://www.qiushibaike.com/8hr/page/"+str(page)+"/"
                # print(url)
                content = requests.get(url,headers=self.headers).text
                # time.sleep(1)
                # print(content)
                self.dataQueue.put(content)

            except Exception as e:
                print(e)
                pass
        print("结束 "+self.threadName)

class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,localFile,lock):
        super(ThreadParse,self).__init__()
        # 线程名
        self.threadName = threadName
        # 数据队列
        self.dataQueue = dataQueue
        # 保存解析后数据的文件名
        self.localFile = localFile
        # 互斥锁
        self.lock = lock

    def run(self):
        print("启动"+self.threadName)
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)

                self.parse(html)
            except Exception as e:
                print(e)
        print("结束" + self.threadName)

    def parse(self,html):
        text = etree.HTML(html)
        # print(text)

        # 返回所有段子的节点位置，contains模糊查询，第一个参数是要匹配的标签，第二个参数是标签名的部分内容
        node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')
        # print(node_list)

        for node in node_list:
            # 用户名
            # username = node.xpath('./div/a/h2')[0].text
            username = node.xpath('./div')[0].xpath(".//h2")[0].text
            # print(username)

            # 图片链接
            image = node.xpath('.//div[@class="thumb"]//@src')  # [0]
            # 取出标签下的内容：段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 点赞,取出标签里包含的内容
            zan = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text

            items = {
                "username": username,
                "content": content,
                "image": image,
                "zan": zan,
                "comments": comments
            }
            # with后面有两个必须执行的操作：__enter__和__exit__，打开和关闭
            # 不管里面的操作如何，都会直接打开和关闭功能
            # 打开锁，向文件添加内容，释放锁
            with self.lock:
                # 写入解析后的数据
                self.localFile.write(json.dumps(items, ensure_ascii=False) + "\n")

CRAWL_EXIT = False #采集网页页码队列是否为空的信号
PARSE_EXIT = False #网页源码队列是否为空的信号

def main():
    #页码队列，存储20个页码，先进先出
    pageQueue = Queue(20)
    #放入1~10的数字，先进先出
    for i in range(1,21):
        pageQueue.put(i)

    #采集结果（网页的HTML源码）的数据队列，参数为空表示不限制
    dataQueue = Queue()
    # 以追加的方式打开本地文件
    localFile = open("duanzi.json","a")

    lock = threading.Lock() #互斥锁

    #三个采集线程的名字
    crawlList = ["采集线程1号","采集线程2号","采集线程3号"]

    #创建、启动和存储三个采集线程
    threadCrawls = []
    for threadName in crawlList:
        thread = ThreadCrawl(threadName,pageQueue, dataQueue)
        thread.start()
        threadCrawls.append(thread)

    # 三个解析线程的名字
    parseList = ["解析线程1号","解析线程2号","解析线程3号"] #
    # 创建、启动和存储三个解析线程
    threadParses = []
    for threadName in parseList:
        thread = ThreadParse(threadName,dataQueue,localFile,lock)
        thread.start()
        threadParses.append(thread)

    while not pageQueue.empty():
        pass
    #如果pageQueue为空，采集线程退出循环
    global  CRAWL_EXIT
    CRAWL_EXIT = True

    print("pageQueue为空")

    for thread in threadCrawls:
        thread.join() #阻塞子线程
        print("1")

    while not dataQueue.empty():
        pass
    # 如果 dataQueue空，解析线程退出循环
    print("dataQueue为空")

    global PARSE_EXIT
    PARSE_EXIT = True

    for thread in threadParses:
        thread.join()
        print("2")

    with lock:
        # 关闭文件，在关闭之前，内容都存在内存里
        localFile.close()


if __name__ == "__main__":
    #main()

    #性能测试
    startTime = time.time()
    main()
    print(time.time() - startTime)


