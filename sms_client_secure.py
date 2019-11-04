import socket

import Crypto
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

client_private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQCLT5ZnO23WWbEiZodJji35W/fIzmp8EJuquObc/6KXU8g+TAor\nw0O5z4TKTwUHiruOc2M3bj6Cb4J5QKE5DRetqDkWkX/Z6Pz7IfACcpXYn0T5RMu8\n1TwrIgBu4EoFjIYGWSMWUg27LO5W45PS4gnhkQGBIbZc5jXnVGRZ4sGt/QIDAQAB\nAoGBAIhDyPIhB0brZIApmZsxH3cRpkUc4ruH4zwSsH7q7bbnlK6a4jf8P3q4qULa\nGClQYjTsWNgXVb1wJUdFGG4diFI7DrXQvtY2I4vRdDbPo14XuPXstL/363fm74fQ\nCEgy65tOUzjr1ziX2E/IrkbgpEixjQneC3DwnfSNQCSEkDsBAkEAu7l7KTQdvVSg\nV8SC4oGPh5x8cP0ZlCVb9VD4Blj9mPemaznX/L7QgKTH//2s/QG/oD98pTJxzRue\nrL1sdS3ipQJBAL36cadHZO6xlG+hAJXy8NbnNgosETNu/JhaS7Dzpl6AzcqEvOIi\nhemXk61g3EI2MkZKvd5qPHQgjpOR5gd79nkCQGfgrmdRgHdpIcUPZ8HBIdRP4oh/\nda0Fs0ofQO/6RHJl77/75SnlyOi2xjlAfX4PfqNFHksni9OMyhQaSa7Z8kUCQQCA\nt9ORt3nXkFI2YCv5bSVpNjcTJVByPNzAjU2Dk1JB7ZuBf/ZKcYGyB5Vzf5E8+2OM\n5M9Ih0p2lCiGK/BjWcZhAkAebdvblQi40LVPHtAUEEAvVQn4v0BGVsGWxa9YVyfF\ngMVj05AYR4a5KwkUWjJdTYkp4Kys5MiJsaldLFaehuEZ\n-----END RSA PRIVATE KEY-----'


def recieve_code():
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        data = s.recv(1024)

        if data:
            # decode data stream
            data = str(data.decode())

            # parse out message sections
            code, signature, server_public_key = data.split('\n\n', 3)

            code = (RSA.importKey(client_private_key)).decrypt(ast.literal_eval(code))
            print('Received: ', code.decode())

            signature = (int(signature),)

            # verify signature
            key = RSA.importKey(server_public_key.encode())
            hash = MD5.new(code).digest()
            if key.verify(hash, signature):
                print("The signature is authentic.")
            else:
                print("The signature is not authentic.")


        s.close()


if __name__ == "__main__":
    recieve_code()
