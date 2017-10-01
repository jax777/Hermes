from DnsServer import dns_server
from multiprocessing import Process
p_dns = Process(target=dns_server, args=())
p_dns.start()
