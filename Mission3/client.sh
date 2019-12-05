ifconfig eth0:0 10.4.10.129/26 up
sysctl net.ipv4.conf.all.accept_redirects=0
/etc/init.d/networking restart
for f in /proc/sys/net/ipv4/conf/*/accept_redirects; do echo 0 > $f; done
ip route add 10.4.10.64/26 via 10.4.10.130
ip route add 10.4.10.65 via 10.4.10.130
