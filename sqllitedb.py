#!/usr/bin/python
# coding: utf-8
# __author__ jax777


import sqlite3
import hashlib
import time
from config import mail, passwd, prefix, datadb

def create_db():
    """
    domains    id  hash domain   stime

    http        id  hash url ua  srcip  time

    dns          id hash domain  srcip  time
    """
    conn = sqlite3.connect(datadb)
    print "Opened database successfully"
    c = conn.cursor()
    c.execute('''CREATE TABLE users
               (
               mail             TEXT,
               passwd           TEXT,
               prefix            TEXT);''')
    print "users created successfully"

    # my user
    c.execute("INSERT INTO users (mail,passwd,prefix)  VALUES ('%s','%s','%s')" % (mail, passwd, prefix))
    conn.commit()

    c.execute('''CREATE TABLE domains
           (
           hash             TEXT,
           domain           TEXT,
           prefix           TEXT,
           stime            TEXT);''')
    print "domains created successfully"

    c.execute('''CREATE TABLE http
               (
                hash         TEXT    NOT NULL,
                url          TEXT    NOT NULL,
                ua           TEXT,
                srcip        TEXT,
                time       TEXT);''')
    print "http created successfully"

    c.execute('''CREATE TABLE dns
                   (
                    hash            TEXT    NOT NULL,
                    domain          TEXT    NOT NULL,
                    srcip           TEXT,
                    time       TEXT);''')
    print "dns created successfully"
    conn.commit()
    conn.close()


def judge_domain(hash,domain,prefix,stime):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    cursor = c.execute("SELECT hash from domains where hash = '%s'" % hash)
    _ = cursor.fetchone()
    if _:
        conn.close()
    else:
        c.execute("INSERT INTO domains (hash,domain,prefix,stime)  VALUES ('%s','%s','%s','%s')" % (hash, domain, prefix, stime))
        conn.commit()
        conn.close()
    return 0


def update_http(hash,url,ua,srcip,time):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    c.execute("INSERT INTO http (hash,url,ua,srcip,time)  VALUES ('%s','%s','%s','%s','%s')" % (hash,url,ua,srcip,time))
    conn.commit()
    conn.close()

def update_dns(hash,domain,srcip,time):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    c.execute("INSERT INTO dns (hash,domain,srcip,time)  VALUES ('%s','%s','%s','%s')" % (hash,domain,srcip,time))
    conn.commit()
    conn.close()

def delet_domain(hash):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()

    c.execute("DELETE from domains where hash = '%s'" % hash)
    c.execute("DELETE from http where hash = '%s'" % hash)
    c.execute("DELETE from dns where hash = '%s'" % hash)
    conn.commit()
    conn.close()

    return 0


## register
def judge_mail(mail):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    cursor = c.execute("SELECT prefix from users where mail = '%s'" % mail)
    _ = cursor.fetchone()
    if _:
        conn.close()
        return 0   # alread registed
    else:
        return 1   # can be new man

def register(mail ,passwd):
    conn = sqlite3.connect(datadb)
    mail = True
    c = conn.cursor()
    prefix = ''
    while mail:
        prefix = hashlib.new('md5', str(time.time())).hexdigest()[0:5]
        mail = c.execute("SELECT mail from users where prefix = '%s'" % prefix).fetchone()

    c.execute("INSERT INTO user (mail,passwd,prefix) VALUES ('%s','%s','%s')" % (mail,passwd,prefix))
    conn.commit()
    conn.close()

def db_login(mail,passwd):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    cursor = c.execute("SELECT prefix from users where mail = '%s' and passwd = '%s'" % (mail,passwd))
    _  = cursor.fetchone()
    if _:
        prefix = _[0]
        conn.close()
        return prefix
    else:
        return 1


## show detalis
def get_domains(prefix):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    cursor = c.execute("SELECT hash,domain,stime from domains where prefix =  '%s'" % prefix)
    domains = []
    for row in cursor:
        _ = {}
        _['hash'] = row[0]
        _['domain'] = row[1]
        _['stime'] = row[2]
        domains.append(_)
    return domains

def get_http_count(hash):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    cursor = c.execute("SELECT count(*) from http where hash =  '%s'" % hash)
    _ = cursor.fetchone()
    if _:
        count = _[0]
        conn.close()
        return count
    else:
        return 'something wrong'

def get_dns_count(hash):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    cursor = c.execute("SELECT count(*) from dns where hash =  '%s'" % hash)
    _ = cursor.fetchone()
    if _:
        count = _[0]
        conn.close()
        return count
    else:
        return 'something wrong'

def get_http_info(hash):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    cursor = c.execute("SELECT url,ua,srcip,time from http where hash =  '%s'" % hash)
    https = []
    for row in cursor:
        _ = {}
        _['url'] = row[0]
        _['ua'] = row[1]
        _['srcip'] = row[2]
        _['time'] = row[3]
        https.append(_)
    return https

def get_dns_info(hash):
    conn = sqlite3.connect(datadb)
    c = conn.cursor()
    cursor = c.execute("SELECT domain,srcip,time from dns where hash =  '%s'" % hash)
    dns = []
    for row in cursor:
        _ = {}
        _['domain'] = row[0]
        _['srcip'] = row[1]

        _['time'] = row[2]
        dns.append(_)
    return dns