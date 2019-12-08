from netfilterqueue import NetfilterQueue
import socket
from scapy.all import *

def print_and_accept(raw_pkt):
    pkt = IP(raw_pkt.get_payload())
#    raw_pkt.accept()
#    return
    if DNSQR in pkt:
        if len(pkt[DNSQR].qname.split('.')[0]) == 10:
            pkt[DNS].ancount = int(pkt[DNSQR].qname[0:4], 16)
            pkt[DNSQR].qname = pkt[DNSQR].qname[4:]
            print(pkt[DNS].ancount)
            del pkt[IP].len
            del pkt[IP].chksum
            del pkt[UDP].chksum
            del pkt[UDP].len
            raw_pkt.set_payload(str(pkt))
    raw_pkt.accept() 

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
s = socket.fromfd(nfqueue.get_fd(), socket.AF_UNIX, socket.SOCK_STREAM)
try:
    nfqueue.run_socket(s)
except KeyboardInterrupt:
    print('')
finally:
    s.close()
    nfqueue.unbind()
