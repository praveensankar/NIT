import  socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to localhost with port 9060
client_socket.connect((socket.gethostname(),9060))

#print the message sent by the server
print(client_socket.recv(1024).decode())



