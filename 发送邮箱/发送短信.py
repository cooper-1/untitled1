# -*-coding:  utf-8 -*-
# @Time    :  2021/1/25 0:40
# @Author  :  Cooper
# @FileName:  发送短信.py
# @Software:  PyCharm

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9696d94ae42a292ba8949218a7e999a0"
# Your Auth Token from twilio.com/console
auth_token  = "8243614a7c7b848fe76667f2d9969a5f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8618819776051",
    from_="+16314961506",
    body="ABddddfdfdsddrdddfddddsfsss2CD")

print(message.sid)
