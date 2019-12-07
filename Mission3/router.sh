ifconfig eth0:0 10.4.10.66/26 up
ifconfig eth0:1 10.4.10.130/26 up
sysctl net.ipv4.ip_forward=1
/etc/init.d/networking restart
iptables -I FORWARD -j NFQUEUE --queue-num 1

iptables -I OUTPUT -p udp --destination-port 53 -j NFQUEUE --queue-num 1
