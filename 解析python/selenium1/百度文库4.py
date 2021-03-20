from selenium import webdriver
import time,re
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"')
driver = webdriver.Chrome(chrome_options=options)
# options = webdriver.ChromeOptions()
# user_ag='MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; '+'CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
# options.add_argument('user-agent=%s'%user_ag)
# driver = webdriver.Chrome(chrome_options=options)
driver.get("https://wenku.baidu.com/view/9816e4ed5122aaea998fcc22bcd126fff7055d86.html")
time.sleep(15)
pattern = re.compile(r'>来自</span><style t(.*?)试读已结束， 剩余0页未读', re.S)
result = pattern.findall(driver.page_source)
result = re.findall(r'[\u4e00-\u9fa5]+',result[0])
with open('baidu.txt','w') as f:
    for index,item in enumerate(result):
        if index%11==0:f.write('\n')
        f.write('  '+item)
driver.quit()