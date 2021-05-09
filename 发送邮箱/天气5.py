# -*-coding:  UTF-8
# @Time    :  2021/4/28 13:03
# @Author  :  Cooper
# @FileName:  天气5.py
# @Software:  PyCharm

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


def main(result):
    # 请自行修改下面的邮件发送者和接收者
    sender = "yx1274814498@163.com"  # 发送方地址
    receivers = ['yx1274814498@163.com','1274814498@qq.com','1506262492@qq.com','1593809016@qq.com']  # "1274814498@qq.com,770031105@qq.com,yx1274814498@163.com"
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = "yx1274814498@163.com"
    message['To'] = 'yx1274814498@163.com,770031105@qq.com,1274814498@qq.com'
    message['Subject'] = Header('1274814498@qq.com示例代码实验邮件', 'utf-8')
    # smtper = SMTP('smtp.163.com',465)
    smtper = smtplib.SMTP_SSL()
    smtper = smtplib.SMTP_SSL('smtp.163.com', 465)
    message = MIMEMultipart('related')
    message['Subject'] = '闰京的 message'

    msgText = MIMEText(result + '<br><img src="cid:image1"></br>', 'html', 'utf-8')
 
    message.attach(msgText)

    fp = open(r'img.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)

    # 请自行修改下面的登录口令
    smtper.ehlo()
    # smtper.starttls()
    smtper.login(sender, "SBMMBSAHCMPDUOWC")  # 此处secretpass输入授权码
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()