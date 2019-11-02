import socket

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast


def main():

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            data = b'Encrypted message'
            conn.sendall(data)

            s.close()


def generate_rsa_keys():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate pub and priv key

    publickey = key.publickey() # pub key export for exchange

    encrypted = publickey.encrypt('encrypt this message', 32)
    decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

    print(decrypted)

    # print(key)



if __name__ == "__main__":
    generate_rsa_keys()
