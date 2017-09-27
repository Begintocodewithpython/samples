# EG14-02 Send packets on port 10001 to another machine

import socket
import time

# You will need to chnge this to the address
# of the machine you are sending to
target_ip = '192.168.1.55'

socket_number = 10006

send_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
destination_address = (target_ip, socket_number)

while(True):
    print('sending')
    send_socket.sendto(b'hello from me', destination_address)
    time.sleep(2)
