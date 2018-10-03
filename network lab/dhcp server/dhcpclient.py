import  socket
import os


max_bytes=65535
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address=(socket.gethostname(),9070)

while True:
    text=''

    client_socket.sendto(text.encode(),('127.0.0.1',9070))

    data,address=client_socket.recvfrom(max_bytes)
    if ('127.0.0.1',9070)==address:
        new_ip_address=data.decode()
        ip_address='sudo ifconfig wlo1 '+new_ip_address
        os.system(ip_address)
        break






