import socket

import Crypto
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random
import ast


client_public_key = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCLT5ZnO23WWbEiZodJji35W/fI\nzmp8EJuquObc/6KXU8g+TAorw0O5z4TKTwUHiruOc2M3bj6Cb4J5QKE5DRetqDkW\nkX/Z6Pz7IfACcpXYn0T5RMu81TwrIgBu4EoFjIYGWSMWUg27LO5W45PS4gnhkQGB\nIbZc5jXnVGRZ4sGt/QIDAQAB\n-----END PUBLIC KEY-----'

server_public_key = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDUykQgqAPT+heQRvx8eE6nZn3m\nDMgse72i0pd5reBxxUdWUzT6dB8nekDoV/JTvEtwdv6UZsSj93Yl9XHKqh9/f4m8\niCUuLtbPPJlw0yd57sy5k4uCrS/oJ0rvWIx3T/RsNnwDqD7YYJ5UWWWq2M1zQhCJ\n4thMLTyEt119Ff3hOwIDAQAB\n-----END PUBLIC KEY-----'
server_private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDUykQgqAPT+heQRvx8eE6nZn3mDMgse72i0pd5reBxxUdWUzT6\ndB8nekDoV/JTvEtwdv6UZsSj93Yl9XHKqh9/f4m8iCUuLtbPPJlw0yd57sy5k4uC\nrS/oJ0rvWIx3T/RsNnwDqD7YYJ5UWWWq2M1zQhCJ4thMLTyEt119Ff3hOwIDAQAB\nAoGAB1GFklH0/79kPBQU7vr8SYme3uClqdH/ra/sgcTXKVKNp4xpEAwaXjM4NEWC\nEhsxxQZyrwvxy2nhaGDOrxe2yY22ZDBLnQapvi8NDMpfJxjY3bfeS2M85snmaWMh\nVjHIr9Z157MXxHnFQHP2/h4K8nuBtqEqC9tK6NabJaZTP+ECQQDcKMz/EV+37XVe\nyl3iTkbpX4exLgEV7nCO8vzARkuL7StEm4TdumD+L/4n+O320paYrxiiNtSdnkKW\nxoINuw3JAkEA925ZT2c/jf5hRbRJwARrILBeGG0Jew5a4ggSOI+eH3hrEJJWPqcK\n28LPzudj8uU5D5OgoKOfYzyRdVGrls9o4wJAGPTTEBLjG9FiHaWo8M9YwHmgwxfo\n7ZiCz+GBfzY4uBrhbbyHWi8XcZj1IYjZSMJkadhnXXQDs/5NpBPKiE3s6QJBAKfC\n/vTyaUoKJsPPGI4DsOrqCfJ/w4TW19IXbNtCrRBjYhxLTASQ17DnJmT/yGnA925T\nRv6D0ibDw1ALPs8y88cCQQCgU1nWJpLntFeZfpO83NIgdpDFjEP7Vt/bxvdR5Aj5\nb3IK0xZS1Yh96GOvLJ8RaafEEp38WAq4E99LelvYZ308\n-----END RSA PRIVATE KEY-----'


def send_code():

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TODO remove?
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            # hash our 2FA code
            code = b'123456'
            hash = MD5.new(code).digest()

            # create signature for hashed code
            rng = Random.new().read
            signature = RSA.importKey(server_private_key).sign(hash, rng)

            # create the message to be sent with the encrypted code
            publickey = RSA.importKey(client_public_key)  # import client public key
            code = publickey.encrypt(code, 32)
            message = str(code[0]) + '\n\n' + str(signature[0]) + '\n\n' + server_public_key.decode()

            # send over our encoded data
            conn.sendall(message.encode())

            s.close()


def generate_rsa_keys():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate pub and priv key

    publickey = key.publickey() # pub key export for exchange

    encrypted = publickey.encrypt('This string was encrypted'.encode('utf-8'), 32)
    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

    print(decrypted)
    print(key.publickey().exportKey('DER'))
    print(key.exportKey('DER'))

    return key



if __name__ == "__main__":
    send_code()
