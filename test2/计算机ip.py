import os
gadslaccount={    'name':'宽带连接',
    'usename':'Administrator',
    'password':'Leimixiusi123'
}
import socket

# 获取本机计算机名称
hostname = socket.gethostname()
print(hostname)
# 获取本机ip
ip = socket.gethostbyname(hostname)
print(ip)
class Adsl(object):
    def __int__(self):
        self.name1=gadslaccount['name']
        self.username=gadslaccount['usename']
        self.password=gadslaccount['password']
    def connect(self):
        cmd_str='rasdial %s %s %s'%(gadslaccount['name'],gadslaccount['usename'],gadslaccount['password'])
        os.system(cmd_str)
    def disconnect(self):
        cmd_str1='rasdial %s'%(gadslaccount['name'])
        os.system(cmd_str1)
    def reconnect(self):
        self.disconnect()
        self.connect()
if __name__ == '__main__':
    A=Adsl()

    A.reconnect()
    # 获取本机计算机名称
    hostname = socket.gethostname()
    print(hostname)
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    print(ip)