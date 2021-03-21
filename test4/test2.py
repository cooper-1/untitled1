# -*-coding:  utf-8 -*-
# @Time    :  2021/3/19 12:56
# @Author  :  Cooper
# @FileName:  test2.py
# @Software:  PyCharm
import random
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome

if __name__ == '__main__':

    f = open('电话.csv', 'a', encoding='utf-8')
    e = open('邮箱.csv','a',encoding='utf-8')
    #
    # f.write('电话\n')
    # e.write('邮箱\n')
    # f.write('关键字：защитная одежда\n')
    # e.write('关键字：защитная одежда\n')
    # f.write('url: https://supl.biz/\n')
    # e.write('url: https://supl.biz/\n')


    from selenium import webdriver
    import time, re

    option = webdriver.ChromeOptions()
    # option.headless=True  #设置选项为无界面
    option = webdriver.ChromeOptions()
    option.add_argument('window-size=1920x1882')  # 指定浏览器分辨率
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    option.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面


# 确定目标的url
    option.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36')
    # 创建selenium实例
    shuo_ = Chrome(options=option)
    # 全屏
    shuo_.maximize_window()

    shuo_.get('https://supl.biz/proposals/search/?query=%D0%9C%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D0%BD%D0%B0%D1%8F%20%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0')
    # 设置等待时间   等待服务器响应
    shuo_.implicitly_wait(5)
    # 窗口最大化
    shuo_.maximize_window()
    time.sleep(10)
    print(shuo_.page_source)
    shuo_.quit()

    #
    # a = 1
    # while True:
    #     try:
    #         time.sleep(5)
    #         shuo_.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]tton').click()
    #         time.sleep(random.randint(1, 2))
    #
    #     except:
    #         print('>>>>>>>商品已全部展现在网页上！！！！！！！')
    #         break
    #     a +=1
    # wb_ = shuo_.find_elements_by_css_selector('.a_3ONW7Mhl')
    # print(len(wb_))
    #
    # for i in range(340,len(wb_)):
    #     # 切换窗口
    #     wei = shuo_.window_handles
    #     shuo_.switch_to_window(wei[0])
    #     time.sleep(8)
    #
    #     # 点击第一个商品   通过分析得知商品的xpath语法是有规律的。比如1-40  40-80
    #     shuo_.find_element_by_xpath(f'//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[{i+1}]').click()
    #     time.sleep(2)
    #
    #     # 切换到商品详情的窗口
    #     wei = shuo_.window_handles
    #     shuo_.switch_to_window(wei[1])
    #     # 点击商品详细信息
    #     time.sleep(3)
    #     #  //*[@id="root"]/div/div[2]/div/div[2]/div[3]/div/div/a
    #     #　//*[@id="root"]/div/div[2]/div/div[2]/div[3]/div/div/a
    #     try:
    #         try:  # 模拟鼠标点击店铺信息
    #             shuo_.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[3]/div/div/a').click()
    #         except:  # 通过调试发现有的时候会报错  找不到这个元素，我把这个报错抛出去   重新点击
    #             time.sleep(2)
    #             shuo_.find_element_by_css_selector('.a_3Kz1iPrx').click()
    #     except:
    #         print('数据全部获取成功！！！ 总共%s条数据'% int(i+1))
    #     # 关闭商品详情页的标签页  减少电脑的负载
    #     time.sleep(2)
    #     shuo_.close()
    #     # 切换串口到店铺的标签页中
    #     wei = shuo_.window_handles
    #     shuo_.switch_to_window(wei[1])
    #
    #     time.sleep(2)
    #     # 提取电话
    #     try:
    #         shuoji_1 = shuo_.find_elements_by_css_selector('.a_2IlHEtj2')
    #         shuoji_1 = [shuoji_1[0].text]
    #         new_tell = []
    #         for dianhua in shuoji_1:
    #             k = dianhua.split(',')
    #
    #             for k_1 in k:
    #                 new_tell.append(k_1)
    #
    #
    #     except:
    #         print(f'第{i+1}条商品,没有电话！！！！！！！！！！！！！！！！')
    #         shuo_.close()
    #         continue
    #
    #
    #
    #
    #     # 提取邮箱地址
    #     try:
    #         shuoji_2 = shuo_.find_elements_by_css_selector('div[class="c_QYnKuwIo c_1vRSxu2U"][style="color:#666666;margin-top:8px"]')[0].text
    #     except:
    #         print(f'第{i+1}条商品,没有邮箱>>>>>>>>>>！！！！！！！！！！！！！！！！')
    #         shuo_.close()
    #         continue
    #     print(f'第{i+1}条数据')     # 电话是：{new_tell[0]},邮箱是：{shuoji_2})
    #     for phone in new_tell:
    #         f.write(f'{phone}\n')
    #         #print(f'电话写入成功数据是{phone}')
    #
    #     e.write(f'{shuoji_2}\n')
    #     #print(f'邮箱写入成功数据是{shuoji_2}~~~~~~~~~~~')
    #     time.sleep(random.randint(5,10))
    #     shuo_.close()
    #
    #
    # print('所有数据已拿到！！ 程序结束>>>>>!!!!')
