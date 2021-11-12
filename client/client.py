import socket
import os
import sys
import time

counter = 0

SRV = os.getenv('SERVER_ADDRESS')
PORT = int(os.getenv('SERVER_PORT'))

while 1:
    if counter != 0:
        time.sleep(5)

    counter += 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (SRV, PORT)
    print("Connection #{}".format(counter))
    print('Connecting to {} port {}'.format(*server_address))
    try:
        sock.connect(server_address)
    except Exception as e:
        print("Cannot connect to the server,", e)
        continue

    try:
        message = b'This is the message. It will be repeated.'
        print('Sending:  {!r}'.format(message))
        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(64)
            amount_received += len(data)
            print('Received: {!r}'.format(data))
    finally:
        print('Closing socket\n')
        sock.close()

