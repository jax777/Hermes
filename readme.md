# 简介
 ***python + tornado + sqlitedb***


 ***dns server** 参考 http://code.activestate.com/recipes/491264-mini-fake-dns-server/

 实现了三个部分，ui（8888端口），http_log（80端口），dns_log（53端口）

## config
 ```
 #!/usr/bin/python
 # coding: utf-8
 # __author__ jax777
 import pytz

 mail = 'test'
 passwd = 'test'
 prefix = 'ke'
 datadb = 'GodEye.db'
 myip = '127.0.0.1'
 mydomain = 'xxx.log'
 tz = pytz.timezone('Asia/Shanghai')
 ```
 config.py中设置了结果简单的配置信息，自行修改即可。

## 公网搭建所需
  - 域名 （用于接收dns请求，将域名的dns服务器地址设置为本服务的ip）
  - vps

## 初次使用
  修改完配置文件，运行 Hermes.py，自动会初始化数据库，

# xip （ssrf探测内网）
 可以使用127.0.0.1.xip.mydomain 来获取内网dns解析


# 风险
 记录数据没过滤，存在注入，然而注入了也没啥用，，不管了

 # db 结构
 ## users
    mail passwd prefix
 ## domains
    hash domain prefix stime
 ## http
    hash url ua srcip time
 ## dns
    hash domain srcip time

# MIT License

    Copyright (c) 2017 jax777

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
