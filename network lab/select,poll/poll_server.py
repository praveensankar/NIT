import select
import socket
import sys
import queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port
server_address = ('localhost', 10001)
print('starting up on %s port %s' % server_address)
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Keep up with the queues of outgoing messages
message_queues = {}

# Do not block forever (milliseconds)
TIMEOUT = 1000

# Commonly used flag setes
READ_ONLY = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
READ_WRITE = READ_ONLY | select.POLLOUT

# Set up the poller
poller = select.poll()
poller.register(server, READ_ONLY)

# Map file descriptors to socket objects
fd_to_socket = { server.fileno(): server,
               }

while True:

    # Wait for at least one of the sockets to be ready for processing
    print('\nwaiting for the next event')
    events = poller.poll(TIMEOUT)

    for fd, flag in events:

        # Retrieve the actual socket from its file descriptor
        s = fd_to_socket[fd]

        # Handle inputs
        if flag & (select.POLLIN | select.POLLPRI):

            if s is server:
                # A "readable" server socket is ready to accept a connection
                connection, client_address = s.accept()
                print('new connection from', client_address)
                connection.setblocking(0)
                fd_to_socket[connection.fileno()] = connection
                poller.register(connection, READ_ONLY)

                # Give the connection a queue for data we want to send
                message_queues[connection] = queue.Queue()

            #s is client
            else:
                data = s.recv(1024)
                if data.decode():
                    # A readable client socket has data
                    print('received "%s" from %s' % (data.decode(), s.getpeername()))
                    message_queues[s]=data.decode()
                    # Add output channel for response
                    poller.modify(s, READ_WRITE)

                else:
                    # Interpret empty result as closed connection
                    print('closing', client_address, 'after reading no data')
                    # Stop listening for input on the connection
                    poller.unregister(s)
                    s.close()

                    # Remove message queue
                    del message_queues[s]

        elif flag & select.POLLOUT:
            # Socket is ready to send data, if there is any to send.
            try:
                next_msg = message_queues[s]
            except queue.Empty:
                # No messages waiting so stop checking for writability.
                print('output queue for', s.getpeername(), 'is empty')
                poller.modify(s, READ_ONLY)
            else:
                print('sending "%s" to %s' % (next_msg, s.getpeername()))
                s.send(next_msg.encode())

