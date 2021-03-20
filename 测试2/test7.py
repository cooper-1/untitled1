# -*-coding:  utf-8 -*-
# @Time    :  2021/2/16 10:33
# @Author  :  Cooper
# @FileName:  test7.py
# @Software:  PyCharm
import os
import re
import requests


def get_response(html_url):
    headers = {'cookie':'__cfduid=d14422a3d37f87b5f44e1b2a850c8d5711613442450; first_visit_datetime_pc=2021-02-16+11%3A27%3A30; p_ab_id=3; p_ab_id_2=3; p_ab_d_id=1837475418; yuid_b=ECAABhc; __guid=68439831.2619759223458332000.1613442450584.5132; __utma=235335808.1436350989.1613442457.1613442457.1613442457.1; __utmz=235335808.1613442457.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=235335808; __utmt=1; __cf_bm=7abb19b2e126a3374af052b0f8e720e5a27a7fa7-1613442456-1800-AbD+89rI1AGZ4m7mPHpPo9xebeG+9mBVJoBLOKt4BskDCav0MgG8QhooItk6Eu56cW41il8mR+Wf7zshxdcvhCXK67X2Ry1nviJcLaGLFNnSH+BoJGykZHLMs8AOqXbF9fuf8ITjcdCD6zSFdMw+cBn6cHPf5S2tDOyp/Z4QARej/kRymvX2jV1cRmZerhwZrg==; _ga=GA1.2.1436350989.1613442457; _gid=GA1.2.1437314758.1613442459; PHPSESSID=63008076_zD1PffEEOlhwhDJWdI8r00PVk8uU46r5; device_token=abd849e55a5ba5d9525df8317951d3f5; c_type=22; privacy_policy_agreement=2; a_type=0; b_type=1; monitor_count=2; __utmv=235335808.|2=login%20ever=no=1^3=plan=normal=1^5=gender=male=1^6=user_id=63008076=1^9=p_ab_id=3=1^10=p_ab_id_2=3=1^11=lang=zh=1; ki_t=1613442480840%3B1613442480840%3B1613442480840%3B1%3B1; ki_r=; ki_s=; tag_view_ranking=qiO14cZMBI~SJK3YcGD-h~RVRPe90CVr~oCR2Pbz1ly~SoxapNkN85~3W4zqr4Xlx~1yIPTg75Rl~Ie2c51_4Sp~5oPIfUbtd6~WVrsHleeCL; tags_sended=1; categorized_tags=qiO14cZMBI; __utmb=235335808.4.10.1613442457',
'Referer': 'https://pixivic.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url=html_url, headers=headers)
    return response


def save(img_url, title):
    path = 'img\\'
    if not os.path.exists(path):
        os.makedirs(path)
    img_data = get_response(img_url).content
    with open(path + title, mode='wb') as f:
        f.write(img_data)
        print(title)


def main(html_url):
    html_data = get_response(html_url).text
    img_url = re.findall('"original":"(.*?)"', html_data)
    title = re.findall('"title":"(.*?)"', html_data)
    picture_data = zip(img_url, title)
    for i in picture_data:
        # 正则匹配的地址
        # https://i.pximg.net/img-original/img/2021/01/03/02/51/59/86774115_p0.jpg
        # 图片真实地址
        # https://original.img.pixivic.net/img-original/img/2021/01/03/02/51/59/86774115_p0.jpg
        picture_1 = i[0].split('net/')[-1]  # img-original/img/2021/01/03/02/51/59/86774115_p0.jpg
        picture_2 = i[0].split('/')[-1]  # 86774115_p0.jpg
        picture_url = 'https://original.img.pixivic.net/' + picture_1
        picture_title = i[1] + picture_2
        save(picture_url, picture_title)


if __name__ == '__main__':
    for page in range(1, 11):
        url = f'https://pix.ipv4.host/ranks?page={page}&date=2021-01-04&mode=day&pageSize=30'
        main(url)