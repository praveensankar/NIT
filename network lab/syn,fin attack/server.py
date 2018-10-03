import  socket
import datetime


server_socket = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)

server_socket.bind(('127.0.0.1',900))

max_bytes=65535
while True:
    (data,address) = server_socket.recvfrom(max_bytes)

    print("client details : ",address,data)


