# -*-coding:  utf-8 -*-
# @Time    :  2021/1/24 23:40
# @Author  :  Cooper
# @FileName:  发送邮箱.py
# @Software:  PyCharm
import smtplib
from email.mime.text import MIMEText

msg_from = "yx1274814498@163.com"  # 发送方地址
pwd = "SBMMBSAHCMPDUOWC"  # 授权密码
to = "yx1274814498@163.com,1274814498@qq.com,770031105@qq.com"  # 接收方地址
# to = "1274814498@qq.com,770031105@qq.com"  # 接收方地址

subject = "天气预报"  # 邮件主题
content = "13℃"  # 邮件内容

# 构造邮件
msg = MIMEText('<html><h1>天气很冷</h1></html>','html','utf-8')   # msg为邮件内容对象
msg["Subject"] = subject
msg["Form"] = msg_from
msg["To"] = to

# 发送邮件
try:
    ss = smtplib.SMTP_SSL("smtp.163.com", 465)  # 465为网易邮箱的端口号  ss是邮件对象
    ss.login(msg_from, pwd)
    ss.sendmail(msg_from, to, msg.as_string())  # 发送邮件
    print("邮件发送成功!")
except Exception as e:
    print("邮件发送失败!错误信息:", e)