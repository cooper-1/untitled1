import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust',
}

path = 'E:\B站\p站/'
repeat = 1


def getSinglePic(url):
    global repeat
    response = requests.get(url, headers=headers)
    # 提取图片名称
    name = re.search('"illustTitle":"(.+?)"', response.text)
    name = name.group(1)
    if re.search('[\\\ \/ \* \? \" \: \< \> \|]', name) != None:
        name = re.sub('[\\\ \/ \* \? \" \: \< \> \|]', str(repeat), name)
        repeat += 1
    # 提取图片原图地址
    picture = re.search('"original":"(.+?)"},"tags"', response.text)
    pic = requests.get(picture.group(1), headers=headers)
    f = open(path + '%s.%s' % (name, picture.group(1)[-3:]), 'wb')
    f.write(pic.content)
    f.close()


def getAllPicUrl():
    count = 1
    for n in range(1, 10 + 1):
        url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust&p=%d&format=json' % n
        response = requests.get(url, headers=headers)
        illust_id = re.findall('"illust_id":(\d+?),', response.text)
        picUrl = ['https://www.pixiv.net/artworks/' + i for i in illust_id]
        for url in picUrl:
            print('正在下载第 %d 张图片' % count, end='   ')
            getSinglePic(url)
            print('下载成功', end='\n')
            count += 1
    return None

getAllPicUrl()