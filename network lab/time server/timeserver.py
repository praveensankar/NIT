import  socket
import datetime

#creating a tcp socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding the socket to localhost with port no 9060
server_socket.bind((socket.gethostname(),9060))

server_socket.listen(10)

while True:
    (client_socket,address) = server_socket.accept()

    print("client details : ",client_socket.getsockname())

    #sending the current time to client
    client_socket.send(str(datetime.datetime.now()).encode())

