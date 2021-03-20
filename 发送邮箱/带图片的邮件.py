# -*-coding:  utf-8 -*-
# @Time    :  2021/1/24 23:55
# @Author  :  Cooper
# @FileName:  带图片的邮件.py
# @Software:  PyCharm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

sender = "yx1274814498@163.com"  # 发送方地址
receiver = ['1274814498@qq.com','yx1274814498@163.com','770031105@qq.com'] #"1274814498@qq.com,770031105@qq.com,yx1274814498@163.com"
subject = 'python email '
smtpserver = 'smtp.163.com'
username = "yx1274814498@163.com"
password = "SBMMBSAHCMPDUOWC"

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'

msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>good!', 'html', 'utf-8')
msgRoot.attach(msgText)

fp = open(r'E:\B站\图片12\36.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()