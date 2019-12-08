from netfilterqueue import NetfilterQueue
import socket
from scapy.all import *

def print_and_accept(raw_pkt):
    pkt = IP(raw_pkt.get_payload())
    if DNSQR in pkt:
        print(pkt[DNS].qr, pkt[DNS].ancount)
        if pkt[DNS].ancount > 0 and pkt[DNS].qr == 0:
            raw_pkt.drop()
            return
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
