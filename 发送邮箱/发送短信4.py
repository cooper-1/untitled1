import requests


class SMS:
    """短信发送功能"""

    def __init__(self, account, password):
        """account:APIID(用户中心【验证码通知短信】-【产品纵览】查看)
           password：APIKEY(用户中心【验证码通知短信】-【产品纵览】查看)
           self.url:接口请求地址
        """
        self.accout = account
        self.passwod = password
        self.url = 'https://106.ihuyi.com/webservice/sms.php?method=Submit'

    def send_sms(self, mobile, content):
        """
            发短信
            :param mobile: 手机号
            :param content: 短信内容
            :return:None
        """
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }

        data = {'account': self.accout,
                'password': self.passwod,
                'mobile': mobile,
                'content': content
                }
        # 发起请求：
        response = requests.post(self.url, headers=headers, data=data)
        print(response.content.decode())


if __name__ == '__main__':
    sms = SMS('C07731612', '7fb40eddd9cdf3017f0c26a551f0edcd')
    sms.send_sms('18819776051', '您好，您的验证码是:666666')

