import socket
import sys
import os

PORT = int(os.getenv('LISTEN_PORT'))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', PORT)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen()

while True:
    print('\nWaiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)
        while True:
            data = connection.recv(64)
            print('Received {!r}'.format(data))
            if data:
                print('Sending data back to the client')
                connection.sendall(data)
            else:
                print('No data from', client_address)
                break
    finally:
        connection.close()
