# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/1/13
#File        : msg.py
#Software    : PyCharm
#finish date :
'''

import time
from twilio.rest import Client

text = 'helloboy'

auth_token =  "8243614a7c7b848fe76667f2d9969a5f"# 去twilio.com注册账户获取token
account_sid = "AC9696d94ae42a292ba8949218a7e999a0"

client = Client(account_sid, auth_token)


def sent_message(phone_number):
    mes = client.messages.create(
        from_='+16314961506',  # 填写在active number处获得的号码
        body=text,
        to=phone_number
    )
    print("OK")


while 1:
    sent_message("+8618819776051")
    sent_message("+8614750622051")
    time.sleep(3600 * 24)