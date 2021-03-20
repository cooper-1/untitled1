"""
    获取bilibili直播间弹幕
    房间号从网页源代码中获取
    打开直播画面后，按ctrl+u 打开网页源代码，按ctrl+f 搜索 room_id
    搜到的"room_id":1016中，1016就是房间号22870638
    获取不同房间的弹幕:修改代码第26行的roomid的值为对应的房间号
"""

import requests;
import time
import pyttsx3

class Danmu():
    def __init__(self):
        # 弹幕url
        self.url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory';
        # 请求头
        self.headers = {
            'Host': 'api.live.bilibili.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        }
        # 定义POST传递的参数
        self.data = {
            'roomid': '22348576',#房间号
            'csrf_token': '',
            'csrf': '',
            'visit_id': '',
        }
        # 日志写对象
        self.log_file_write = open('danmu.log', mode='a+', encoding='utf-8');
        # 读取日志
        log_file_read = open('danmu.log', mode='r', encoding='utf-8');
        self.log = log_file_read.readlines();

    def get_danmu(self):
        # 获取直播间弹幕
        html = requests.post(url=self.url, headers=self.headers, data=self.data).json();
        #print( requests.post(url=self.url, headers=self.headers, data=self.data).text)
        # 解析弹幕列表
        for content in html['data']['room']:
            # 获取昵称
            nickname = content['nickname'];
            # 获取发言
            text = content['text'];
            # 获取发言时间
            timeline = content['timeline'];
            # 记录发言
            msg2=nickname + ': ' + text
            msg = timeline + ' ' + nickname + ': ' + text;
            # 判断对应消息是否存在于日志，如果和最后一条相同则打印并保存
            if msg + '\n' not in self.log:
                # 打印消息
                print(msg);
                speaker(msg2)
                # 保存日志
                self.log_file_write.write(msg + '\n');
                # 添加到日志列表
                self.log.append(msg + '\n');

def speaker(msg):
    # msg = '''盼望着，盼望着，东风来了，春天的脚步...'''
    teacher = pyttsx3.init()
    rate = teacher.getProperty('rate')
    teacher.setProperty('rate', rate -20)
    teacher.say(msg)
    teacher.runAndWait()

if __name__ == '__main__':
    # 创建bDanmu实例
    bDanmu = Danmu();
    while True:
        # 暂停1秒防止cpu占用过高
        time.sleep(1);
        # 获取弹幕
        bDanmu.get_danmu();