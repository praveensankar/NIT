import select
import socket
import sys
import queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#non blocking socket
server.setblocking(0)

# Bind the socket to the port
server_address = ('localhost', 10001)
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

# Sockets from which we expect to read
inputs = [ server ]

# Sockets to which we expect to write
outputs = [ ]

# Outgoing message queues (socket:Queue)
message_queues = {}


while inputs:

    # Wait for at least one of the sockets to be ready for processing
    print(  '\nwaiting for the next event')
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    # Handle inputs
    for s in readable:

        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            print(  'new connection from', client_address)
            connection.setblocking(0)
            inputs.append(connection)


        else:
            data = s.recv(1024)
            if data.decode():
                # A readable client socket has data
                print(  'received "%s" from %s' % (data.decode(), s.getpeername()))
                message_queues[s]=data.decode()
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)

            else:
                # Interpret empty result as closed connection
                print(  'closing', client_address, 'after reading no data')
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # Remove message queue
                del message_queues[s]

# Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s]
        except queue.Empty:
            # No messages waiting so stop checking for writability.
            print(  'output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)
        else:
            print(  'sending "%s" to %s' % (next_msg, s.getpeername()))
            s.send(next_msg.encode())

# Handle "exceptional conditions"
    for s in exceptional:
        print(  'handling exceptional condition for', s.getpeername())
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del message_queues[s]