#!/usr/bin/env python

import sys
import thread
import socket
import hashlib
import traceback
import datetime

from sqllitedb import judge_domain
from sqllitedb import update_dns
from config import myip, mydomain
from config import tz


# DNSQuery class from http://code.activestate.com/recipes/491264-mini-fake-dns-server/
class DNSQuery:
    def __init__(self, data):
        self.data = data
        self.domain = ''

        tipo = (ord(data[2]) >> 3) & 15  # Opcode bits
        if tipo == 0:  # Standard query
            ini = 12
            lon = ord(data[ini])
            while lon != 0:
                self.domain += data[ini + 1:ini + lon + 1] + '.'
                ini += lon + 1
                lon = ord(data[ini])

    def respuesta(self, ip):
        packet = ''
        if self.domain:
            packet += self.data[:2] + "\x81\x80"
            packet += self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'  # Questions and Answers Counts
            packet += self.data[12:]  # Original Domain Name Question
            packet += '\xc0\x0c'  # Pointer to domain name
            packet += '\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'  # Response type, ttl and resource data length -> 4 bytes
            packet += str.join('', map(lambda x: chr(int(x)), ip.split('.')))  # 4bytes of IP
        return packet




def usage():
    print ""
    print "Usage:"
    print ""
    print "\t# SimpleDNSServer [hosts file]"
    print ""
    print "Description:"
    print ""
    print "\tSimpleDNSServer will redirect DNS query to local machine."
    print ""
    print "\tYou can optionally specify a hosts file to the command line:\n"
    print "\t\t# SimpleDNSServer hosts\n"
    print "\tThe ip address will be chosen prior to system hosts setting and remote dns query from local machine. \n"
    print "\tIf SimpleDNSServer and the DNS setting machine are same, you should set an optional DNS server in the DNS setting to avoid DNS query failure caused by redirecting recursively.\n"
    print ""



def domain_log(domain,sip):
    hash = hashlib.new('md5', domain).hexdigest()
    stime = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    try:
        if mydomain in domain:
            prefix = domain.split('.')[-3]
            judge_domain(hash, domain, prefix, stime)
    except Exception,e:
        traceback.print_exc()
    update_dns(hash, domain, sip, stime)


def query_and_send_back_ip(udps,data, addr):
    try:
        p = DNSQuery(data)
        domain = p.domain[:-1]
        #print 'Request domain: %s' % p.domain
        xip = 'xip.' + mydomain
        if xip == domain[-len(xip):]:
            ip =  domain[:-len(xip)-1]
        else:
            ip = myip
        udps.sendto(p.respuesta(ip), addr)
        domain_log(domain,addr[0])
        #print p.domain
        #print 'Request: %s -> %s' % (p.domain, myip)
    except Exception, e:
        print 'query for:%s error:%s' % (p.domain, e)




def dns_server():
    try:
        udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udps.bind(('', 53))
    except Exception, e:
        print "Failed to create socket on UDP port 53:", e
        sys.exit(1)
    try:
        while 1:
            data, addr = udps.recvfrom(1024)
            thread.start_new_thread(query_and_send_back_ip, (udps,data, addr))
    except KeyboardInterrupt:
        print '\n^C, Exit!'
    except Exception, e:
        print '\nError: %s' % e
    finally:
        udps.close()