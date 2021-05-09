# -*-coding:  UTF-8
# @Time    :  2021/4/28 11:17
# @Author  :  Cooper
# @FileName:  天气2.py
# @Software:  PyCharm
from os import system

import sys
import importlib

importlib.reload(sys)


sys.setdefaultencoding('utf8')

import smtplib
def mail():

   from_addr = "yx1274814498@163.com" # email addresss include domain name 

   password = "SBMMBSAHCMPDUOWC"# password 
   to_addr = '1274814498@qq.com'# target email address 

   smtp_server = "smtp.qq.com" # smtp sever domain for qq is smtp.qq.com  
   msg = MIMEText('hello, send by python !!!', 'plain', 'utf-8')

   msg['Subject'] = Header("test auto send mail", 'utf-8')

   msg['from'] = from_addr

   msg['to'] = to_addr



   server = smtplib.SMTP_SSL()#   server = smtplib.SMTP()

# server.set_debuglevel(1)

   # server.connect(smtp_server, 465)

   server = smtplib.SMTP_SSL(smtp_server,465)

   server.ehlo(smtp_server)

   server.login(from_addr, password)

   server.sendmail(from_addr, to_addr, msg.as_string())

   server.quit()

   print('email has send out !')

   return True

mail()