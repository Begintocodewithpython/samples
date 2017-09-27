# EG14-01 Receive packets on port 10001 from another machine

import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('The ip address of this computer is:', host_ip)

listen_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
listen_address = (host_ip, 10006)

listen_socket.bind(listen_address)

print('Listening:')

while(True):
    reply = listen_socket.recvfrom(4096)
    print(reply)
