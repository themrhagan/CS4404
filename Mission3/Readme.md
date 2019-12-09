###Mission 3
This mission is split between four different scripts that can be run on two different machines. client.py and dns_answer_counter_changer.py are run on one machine and ids.py and dns_server.py are run on a different machine.

####client.py
This script will read a file from the computer and send the data from it to the dns server. The data will be packed into the subdomain of the the DNS query in order to be read from the intermediate script, dns_answer_counter_changer.py, and packed into the ancount field.

####dns\_answer\_counter\_changer.py
This script will intercept the packets trying to leave the first machine and modify them to stuff in the checksum value from the subdomain. Any subdomains with a length of 10 will have their qname field inspected to place the checksum bytes into the ancount and remove them from the qname field. The modified packet will be outputted back onto the stream.

####ids.py
This script runs on a different machine and will detect and drop any packets with an ancount greater than 0 and a qr equal to 0. If a packet does not meet these conditions, it will be forwarded.

####dns_server.py
The script is a DNS server that will return an IP address for the requested DNS query.
