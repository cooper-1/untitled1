#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : ShiMeng
# @File    : send_sms.py
# @Software: PyCharm
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC9696d94ae42a292ba8949218a7e999a0"
# Your Auth Token from twilio.com/console
auth_token  = "8243614a7c7b848fe76667f2d9969a5f"
client = Client(account_sid, auth_token)
message = client.messages.create(
    # 这里中国的号码前面需要加86
    to="+8614750622051",
    from_="+16314961506",
    body="Hello from Python!")
print(message.sid)