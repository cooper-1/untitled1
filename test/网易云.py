# 引入相关库
import requests
from bs4 import BeautifulSoup
import urllib.request


class LoadWYMusic:  # 下载指定网易云歌单歌曲到本地
    def __init__(self, url):
        self.music_list_url = url
        self.music_base_outer_url = 'http://music.163.com/song/media/outer/url'
        # 伪装爬虫
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
        }

    def parser_url(self, url):
        """ 解析网址
        :param url: 网址
        :return: 网址响应内容
        """
        print(url)
        response = requests.get(url, headers=self.headers)
        with open("musiclist.txt", "w", encoding="utf-8") as f:
            f.write(response.content.decode())
        return response.content.decode()

    def get_music_list(self, music_content):
        """ 获取歌曲列表，并生成歌曲下载列表
        :param music_content: 歌曲内容
        :return: 歌曲列表
        """
        # 使用bs4匹配出对应的歌曲名称和地址
        s = BeautifulSoup(music_content, 'lxml')
        music_content_items = s.find('ul', class_="f-hide")
        print(music_content_items)
        music_list = []
        for music_item in music_content_items.find_all("a"):
            music_dic = {}
            print(music_item)
            print("{} : {} ".format(music_item.text, music_item["href"]))

            # 把信息保存到字典，再添加到列表中
            music_dic["music_name"] = music_item.text
            music_dic["music_url"] = self.music_base_outer_url + music_item["href"][5:] + ".mp3"
            music_list.append(music_dic)

        return music_list

    def load_save_musics(self, musics_list):
        """ 根据列表，下载歌曲
        :param musics_list:
        :return:
        """
        music_counter = 0
        print(musics_list)
        for music in musics_list:
            name = music["music_name"]
            url = music["music_url"]
            try:
                print("开始下载歌曲：%s ..." % name)
                urllib.request.urlretrieve(url, "%s.mp3" % name)
                print("%s 下载成功" % name)
                music_counter += 1
            except:
                print("%s 下载失败" % name)

        print("歌曲下载完成")
        return music_counter

    def run(self):
        # 1、获取歌曲内容网页
        music_html = self.parser_url(self.music_list_url)
        # 2、解析成歌曲列表
        musics_list = self.get_music_list(music_html)
        # 3、根据列表信息，下载歌曲
        music_amount = self.load_save_musics(musics_list)
        print("下载成功 %d 首歌曲" % music_amount)


if __name__ == "__main__":
    # 歌曲地址 原网址 https://music.163.com/#/playlist?id=2272699928
    url = "http://music.163.com/playlist?id=2272699928"  # 网址修改包装
    load_wy_music = LoadWYMusic(url)
    load_wy_music.run()