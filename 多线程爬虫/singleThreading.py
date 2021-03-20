from lxml import etree  # 解析库
import requests          # 请求处理
import json              # json处理
import time

# 访问网页的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/52.0.2743.116 Safari/537.36', 'Accept-Language': 'zh-CN,zh;q=0.8'}
# 存储解析后数据的本地文件
local_file = open("duanzi.json", "a")


# 解析html字符串，获取需要的信息
def parse_html(html):
    text = etree.HTML(html)
    # 返回所有段子的节点位置
    # contains模糊查询，第一个参数是要匹配的标签，第二个参数是标签名的部分内容
    node_list = text.xpath('//div[contains(@id,"qiushi_tag")]')
    for node in node_list:
        try:
            # 用户名
            username = node.xpath('./div')[0].xpath(".//h2")[0].text
            # 图片链接
            image = node.xpath('.//div[@class="thumb"]//@src')  # [0]
            # 取出标签下的内容：段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 点赞,取出标签里包含的内容
            like = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text
            # 构建json格式的字符串
            items = {
                "username": username,
                "content": content,
                "image": image,
                "zan": like,
                "comments": comments
            }
            # 写入存储的解析后的数据
            local_file.write(json.dumps(items, ensure_ascii=False) + "\n")
        except:
            pass


def main():
    # 循环获取第1~20页共20页的网页源码，并解析
    for page in range(1, 21):
        # 每个网页的网址
        url = "http://www.qiushibaike.com/8hr/page/" + str(page) + "/"
        # 爬取网页源码
        html = requests.get(url, headers=headers).text
        # 解析网页信息
        parse_html(html)


# 程序运行入口
if __name__ == '__main__':
   # main()

    # 性能分析
    startTime = time.time()
    main()
    print(time.time() - startTime)

