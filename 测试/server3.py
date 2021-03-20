upstream
websocket
{
    server127.0
.0
.1: 12121;
}

server
{
    listen
443;
server_name
___aaa___.com;
index
index.html
index.htm
index.php
default.html
default.htm
default.php;
root / ___aaa___;

# include none.conf;
# error_page   404   /404.html;
include
enable - php - pathinfo.conf;

ssl
on;
ssl_certificate / ___aaa___.pem;
ssl_certificate_key / ___aaa___.key;
ssl_session_timeout
5
m;
ssl_ciphers
ECDHE - RSA - AES128 - GCM - SHA256: ECDHE:ECDH: AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
ssl_protocols
TLSv1
TLSv1
.1
TLSv1
.2;
ssl_prefer_server_ciphers
on;

# 用于小程序的 websocket 连接
location / wss
{
    proxy_pass
http: // websocket;
# 代理到上面的地址去
proxy_http_version
1.1;
proxy_set_header
Upgrade $http_upgrade;
proxy_set_header
Connection
"Upgrade";
}

location / {
    # 主项目
}

location
~.* \.(gif | jpg | jpeg | png | bmp | swf)$
{
    expires
30
d;
}

location
~.* \.(js | css)?$
{
    expires
12
h;
}

location
~ /\.
{
    deny
all;
}

access_log / ___aaa___.log;
}
