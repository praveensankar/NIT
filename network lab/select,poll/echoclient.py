import socket
import sys

messages = [ 'This is the message. ',
             'It will be sent ',
             'in parts.',
             ]
server_address = ('localhost', 10001)

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
socket.socket(socket.AF_INET, socket.SOCK_STREAM),
socket.socket(socket.AF_INET, socket.SOCK_STREAM),
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          ]

# Connect the socket to the port where the server is listening
print(  'connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for s in socks:
        print(  '%s: sending "%s"' % (s.getsockname(), message))
        s.send(message.encode())

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print(  '%s: received "%s"' % (s.getsockname(), data.decode()))
        if not data.decode():
            print(  'closing socket', s.getsockname())
            s.close()