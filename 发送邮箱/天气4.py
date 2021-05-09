# -*-coding:  UTF-8
# @Time    :  2021/4/28 13:02
# @Author  :  Cooper
# @FileName:  天气4.py
# @Software:  PyCharm

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
import smtplib


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = "yx1274814498@163.com"  # 发送方地址
    receivers = ['yx1274814498@163.com','1274814498@qq.com','1506262492@qq.com','1593809016@qq.com']  # "1274814498@qq.com,770031105@qq.com,yx1274814498@163.com"

    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = "yx1274814498@163.com"
    message['To'] = '1274814498@qq.com'
    message['Subject'] = Header('1274814498@qq.com示例代码实验邮件', 'utf-8')
    # smtper = SMTP('smtp.163.com',465)
    smtper = smtplib.SMTP_SSL()
    smtper = smtplib.SMTP_SSL('smtp.163.com', 465)

    # 请自行修改下面的登录口令
    smtper.ehlo()
    # smtper.starttls()
    smtper.login(sender, "SBMMBSAHCMPDUOWC")  # 此处secretpass输入授权码
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()