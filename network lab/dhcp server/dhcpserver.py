import  socket
import datetime


server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_socket.bind(('127.0.0.1',9070))

max_bytes=65535
while True:
    (data,address) = server_socket.recvfrom(max_bytes)

    print("client details : ",address)
    ip='172.18.5.31'
    server_socket.sendto(ip.encode(),address)

