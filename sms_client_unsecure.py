import socket


def recieve_code():
    HOST = '10.4.10.65'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        data = s.recv(1024)

        if data:
            # decode data into code
            code = str(data.decode())
            print('Received: ', code)


        s.close()


if __name__ == "__main__":
    recieve_code()
