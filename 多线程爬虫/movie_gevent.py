import requests
from queue import Queue
from lxml import etree
import gevent
import time
from gevent import  monkey
monkey.patch_all()

class Spider(object):
    def __init__(self):
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.base_url = "https://www.qiushibaike.com/8hr/page/"
        # 创建保存数据的队列
        self.data_queue = Queue()
        # 统计数量
        self.count = 0

    def send_request(self, url):
        print("[INFO]: 正在抓取" + url)
        html = requests.get(url, headers=self.headers).content
        # 每次请求间隔1秒
        time.sleep(1)
        self.parse_page(html)

    def parse_page(self, html):
        html_obj = etree.HTML(html)
        node_list = html_obj.xpath('//div[contains(@id,"qiushi_tag")]')
        for node in node_list:
            # 用户名
            username = node.xpath('./div')[0].xpath(".//h2")[0].text
            # 图片链接
            image = node.xpath('.//div[@class="thumb"]//@src')
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
            self.count += 1
            self.data_queue.put(items)

    def start_work(self):
        job_list = []
        for page in range(1, 14):
            # 创建一个协程任务对象
            url = self.base_url + str(page) + "/"
            job = gevent.spawn(self.send_request, url)
            # 保存所有的协程任务
            job_list.append(job)
        # joinall()接收一个列表，将列表里的所有协程任务添加到任务队列里执行
        gevent.joinall(job_list)
        local_file = open("duanzi.txt", "wb+")
        while not self.data_queue.empty():
            content = self.data_queue.get()
            result = str(content).encode("utf-8")
            local_file.write(result + b'\n')
        local_file.close()
        print(self.count)

if __name__ == "__main__":
    # spider = Spider()
    # spider.start_work()

    # 性能分析
    spider = Spider()
    start = time.time()
    spider.start_work()
    print("[INFO]: Useing time %f secend" % (time.time() - start))

