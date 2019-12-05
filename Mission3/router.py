from netfilterqueue import NetfilterQueue
#from scapy.all import *

def print_and_accept(raw_pkt):
        print(raw_pkt)
        raw_pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print
