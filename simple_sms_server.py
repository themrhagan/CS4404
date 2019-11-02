import socket

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast


database = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCLT5ZnO23WWbEiZodJji35W/fI\nzmp8EJuquObc/6KXU8g+TAorw0O5z4TKTwUHiruOc2M3bj6Cb4J5QKE5DRetqDkW\nkX/Z6Pz7IfACcpXYn0T5RMu81TwrIgBu4EoFjIYGWSMWUg27LO5W45PS4gnhkQGB\nIbZc5jXnVGRZ4sGt/QIDAQAB\n-----END PUBLIC KEY-----'

def send_code():

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            publickey = RSA.importKey(database)

            data = b'Encrypted message'

            data = publickey.encrypt(data, 32)
            print(str(data).encode())

            conn.sendall(str(data).encode())

            s.close()


def generate_rsa_keys():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate pub and priv key

    publickey = key.publickey() # pub key export for exchange

    encrypted = publickey.encrypt('This string was encrypted'.encode('utf-8'), 32)
    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

    print(decrypted)
    print(key.publickey().exportKey('PEM'))
    print(key.exportKey('PEM'))



if __name__ == "__main__":
    send_code()
