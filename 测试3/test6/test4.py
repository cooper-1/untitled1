# -*-coding:  UTF-8
# @Time    :  2021/4/6 18:38
# @Author  :  Cooper
# @FileName:  test4.py
# @Software:  PyCharm

import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
import random
from selenium import webdriver
import time, re

j = 0
user_agent_list = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

header={
'authority': 'www.pixiv.net',
'method': 'GET',
'path': '/ajax/user/26110675/illusts?ids%5B%5D=88211011&ids%5B%5D=87115159&ids%5B%5D=87092008&ids%5B%5D=86949216&ids%5B%5D=86907470&ids%5B%5D=86715108&ids%5B%5D=86548863&ids%5B%5D=86372973&ids%5B%5D=86193944&ids%5B%5D=86085150&ids%5B%5D=86048387&ids%5B%5D=85902881&ids%5B%5D=85835402&ids%5B%5D=85564820&ids%5B%5D=85531474&ids%5B%5D=85458316&ids%5B%5D=85436081&ids%5B%5D=85412499&lang=zh',
'scheme': 'https',
'accept': 'application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cookie': 'first_visit_datetime_pc=2021-02-16+11%3A27%3A30; p_ab_id=3; p_ab_id_2=3; p_ab_d_id=1837475418; yuid_b=ECAABhc; __guid=68439831.2619759223458332000.1613442450584.5132; __utmz=235335808.1613442457.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1436350989.1613442457; PHPSESSID=63008076_zD1PffEEOlhwhDJWdI8r00PVk8uU46r5; c_type=22; privacy_policy_agreement=2; a_type=0; b_type=1; ki_r=; __gads=ID=8d92494c1e281921:T=1613442924:S=ALNI_MZbYDuEemwTiIJtD5kAUvC1a03Y2Q; ki_t=1613442480840%3B1615184883391%3B1615184883391%3B2%3B2; ki_s=214027%3A0.0.0.0.2; __cfduid=d3e4cb19978e64b6a0624355a1abfd8a71617706975; __utma=235335808.1436350989.1613442457.1615184827.1617706982.3; __utmc=235335808; _gid=GA1.2.1555570954.1617708493; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=63008076=1^9=p_ab_id=3=1^10=p_ab_id_2=3=1^11=lang=zh=1; tags_sended=1; categorized_tags=6sZKldb07K~DN6RDM1CuJ~LxdXI7-B2R~ea8DYxYsty~qiO14cZMBI; user_language=zh; __utmt=1; __cf_bm=52659630cc27deb25e1b7d1f5cf1f5ce9bc65580-1617709556-1800-AfULjAsyv9fRyRn7dwkkpG1/hxfQ+icZsJQzsPc9zfQn6sptg1T8zaLil9Xd0FlvKe4SWgvIO7FdIbaMMeTwgQDIJpWzClK6qZsJBV16LfSZVPeueMwwCvxSciDJVuDM20Gce2fuLrs1iat+0GxRjn7PFc6yQ5/4WKo80j1TV17YUNjhLVjOwhil121Btfc96A==; _gcl_au=1.1.1463566566.1617709804; tag_view_ranking=RVRPe90CVr~qiO14cZMBI~oCR2Pbz1ly~SJK3YcGD-h~n7YxiukgPF~ea8DYxYsty~moEyDUmkHh~BAOGRD22OG~LxdXI7-B2R~V0wxmDLlG5~SoxapNkN85~3W4zqr4Xlx~1yIPTg75Rl~Ie2c51_4Sp~5oPIfUbtd6~WVrsHleeCL; __utmb=235335808.9.10.1617706982; OX_plg=swf|sl|wmp|shk|pm; monitor_count=9',
'referer': 'https://www.pixiv.net/artworks/88811788',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'x-user-id': '63008076',
}
def getlist(url):
    try:  # 获取列表URL
        global j
        j += 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=20)
        print('第%s轮，第一次·网络状态码: ' % j, res.status_code, url)
        print(res.content.decode('utf-8'))
        pattern = re.compile(r'<h4 class="jobName" id="h4JobTitle">(.*?)提醒：以担保或任何理由向求职者索取财物，扣押证照，均涉嫌违法。请您提高警惕。', re.S)
        result = pattern.findall(res.content.decode('utf-8'))
        print(result)

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)

def get(url):
    options = webdriver.ChromeOptions()
    # options.headless = True  # 设置选项为无界面
    options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    print(driver.page_source)
    # pattern = re.compile(r'"JobPositionNumber":"(.*?)"', re.S)
    # result = pattern.findall(driver.page_source)
    driver.quit()
    # return result

if __name__ == '__main__':
    url='https://embed.pixiv.net/decorate.php'
    # url='https://www.pixiv.net/artworks/88811788'
    # get(url)
    getlist(url)
    #https://www.pixiv.net/artworks/88811788


