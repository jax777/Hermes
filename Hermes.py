#!/usr/bin/python
# coding: utf-8
# __author__ jax777

import os
import cgi
import json
import urllib
import hashlib
import datetime
import tornado.ioloop
import tornado.web
import traceback
from tornado.escape import json_decode
from multiprocessing import Process
from sqllitedb import *
from DnsServer import dns_server
from config import datadb
from config import mydomain
from config import tz


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        print self.get_secure_cookie("prefix")
        return self.get_secure_cookie("prefix")

class login(tornado.web.RequestHandler):
    #  页面跳转 /#/info
    def get(self):
        pass
    def post(self):
        data = json_decode(self.request.body)
        mail = data['mail']
        passwd = data['passwd']
        try:
            prefix = db_login(mail,passwd)
            if prefix == 1:
                self.write("0")
            else:
                self.set_secure_cookie("prefix", prefix)
                self.write("1")
        except  Exception,e:
            traceback.print_exc()
            self.write("0")


class getDomain(tornado.web.RequestHandler):
   # @tornado.web.authenticated
    def get(self):
        prefix = self.get_secure_cookie("prefix")
        #print prefix
        if prefix:
            domains = get_domains(prefix)
            # hash domain stime
            ret = []
            #print domains
            for tmp in domains:
                httpcount = get_http_count(tmp['hash'])
                dnscount = get_dns_count(tmp['hash'])
                _ = {'hash': tmp['hash'],'domain':tmp['domain'],'http':httpcount,'dns':dnscount,'time':tmp['stime']}
                ret.append(_)
            self.write(json.dumps(ret))
        else:
            self.write("0")
class showHttp(tornado.web.RequestHandler):
    # @tornado.web.authenticated
    def get(self,hash):
        http = get_http_info(hash)
        info = ''
        for tmp in http:
            url = urllib.unquote(tmp['url'])
            info = info + url + 'user-agent:'+ tmp['ua'] + '   srcip:' + tmp['srcip'] + '   time:' + tmp['time'] + '\n'
            info = cgi.escape(info)
        # write  base64 txt

        self.write(info)

class showDns(tornado.web.RequestHandler):
    # @tornado.web.authenticated
    def get(self,hash):
        dns = get_dns_info(hash)
        info = ''
        for tmp in dns:
            info = info + 'domain:' + tmp['domain'] + '    srcip:' + tmp['srcip'] + '    time:' + tmp['time'] + '\n'
            info = cgi.escape(info)
        self.write(info)

class deletDomain(tornado.web.RequestHandler):
    # @tornado.web.authenticated
    def get(self,hash):
        delet_domain(hash)
        self.write('1')

class deletALL(tornado.web.RequestHandler):
    # @tornado.web.authenticated
    def get(self):
        self.write("1")

class index(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

def ui():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "login_url": "/#/",
        "cookie_secret":"tw51dk+wR3iErYBKKKpFwHF20ppWjUBHut3b1cCoWmw="
    }
    return tornado.web.Application([
        (r"/login", login),
        (r"/getDomain", getDomain),
        (r"/showHttp/([0-9a-z]{32})", showHttp),
        (r"/showDns/([0-9a-z]{32})", showDns),
        (r"/deletDomain/([0-9a-z]{32})", deletDomain),
        (r"/deletAll", deletALL),
        (r"/", index),
    ], **settings)






class http_handler(tornado.web.RequestHandler):
    def get(self):
        url = self.request.protocol + "://" + self.request.host + self.request.uri
        url = urllib.quote(url)
        srcip = self.request.remote_ip
        ua = ''
        hash = hashlib.new('md5', self.request.host).hexdigest()
        stime = datetime.datetime.now(tz).strftime( '%Y-%m-%d %H:%M:%S' )
        try:
            if mydomain in self.request.host:
                prefix =  self.request.host.split('.')[-3]
                judge_domain(hash,self.request.host,prefix,stime)
        except Exception,e:
            traceback.print_exc()
        #id = """"""
        try:
            ua = self.request.headers["User-Agent"]
        except:
            pass
        update_http(hash,url,ua,srcip,stime)
        self.write("hello moto")



def http_log():
    return tornado.web.Application([
        (r".*", http_handler),
    ])


if __name__ == "__main__":
    if os.path.exists(datadb):
        pass
    else:
        create_db()
    UI = ui()
    UI.listen(8888)
    print 'UI done'

    p_dns = Process(target=dns_server, args=())
    p_dns.start()
    print 'dns done'

    http_server = http_log()
    http_server.listen(80)
    print 'http done'

    tornado.ioloop.IOLoop.current().start()