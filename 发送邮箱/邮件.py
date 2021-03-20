# -*-coding:  utf-8 -*-
# @Time    :  2021/3/6 20:59
# @Author  :  Cooper
# @FileName:  邮件.py
# @Software:  PyCharm
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

msgText = MIMEText('''<li class="sky skyid lv3 on">
<h1>6日（今天）</h1>
<big class="png40"></big>
<big class="png40 n02"></big>
<p title="阴" class="wea">阴</p>
<p class="tem">
<i>13℃</i>
</p>
<p class="win">
<em>
<span title="无持续风向" class="NNW"></span>
</em>
<i>&lt;3级</i>
</p>
<div class="slid"></div>
</li>''', 'html', 'utf-8')
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
print('发送成功')
smtp.quit()