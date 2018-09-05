import socket

sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM,0)
while True:
    hostname = input("please enter the hostname to get ip address : ")
    print(socket.gethostbyname(hostname))
    ipaddr = input("please enter the ipaddress to get host name : ")
    print(socket.gethostbyaddr(ipaddr))
