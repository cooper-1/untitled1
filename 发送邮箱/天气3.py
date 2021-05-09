# -*-coding:  UTF-8
# @Time    :  2021/4/28 12:49
# @Author  :  Cooper
# @FileName:  天气3.py
# @Software:  PyCharm
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender = "yx1274814498@163.com"  # 发送方地址
receive = 'yx1274814498@163.com,1274814498@qq.com,1506262492@qq.com,1593809016@qq.com'
passwd = "SBMMBSAHCMPDUOWC" # 授权码
mailserver = 'smtp.163.com'
port = '465'
sub = 'TEST RESULT' # 邮件主题


msg = MIMEMultipart('related')
msg['From'] = formataddr(["yx1274814498@163.com", sender])
msg['To'] = formataddr(["yx1274814498@163.com,1274814498@qq.com,", receive])
msg['Subject'] = sub

txt = MIMEText('This is your test result！', 'plain', 'utf-8')
msg.attach(txt)

# 添加附件，以txt为例，可以改成其他文件格式
attach = MIMEApplication(open(r'img.jpg', 'rb').read())
attach.add_header('Content-ID', '<image1>')
msg.attach(attach)
server = smtplib.SMTP_SSL(mailserver, port)
server.login(sender, passwd)
server.sendmail(sender, receive, msg.as_string())
server.quit()