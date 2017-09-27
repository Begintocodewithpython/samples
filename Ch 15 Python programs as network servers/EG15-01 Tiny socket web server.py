# EG15-01 Tiny socket web server

import socket

host_ip = 'localhost'
host_socket = 8080

full_address = 'http://' + host_ip + ':' + str(host_socket)

print('Open your browser and connect to: ', full_address) 

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_address = (host_ip, host_socket)

listen_socket.bind(listen_address)
listen_socket.listen()

connection, address = listen_socket.accept()
print('Got connection from: ', address)

network_message_bytes = connection.recv(1024)  
html_request_string = network_message_bytes.decode() 
print(html_request_string)

status = 'HTTP/1.1 200 OK'

header = '''Content-Type: text/html; charset=UTF-8
Connection: close

'''

content='''<html>
<body>
<p>hello from our tiny server</p>
</body></html>

'''

response_string = status + header + content

response_bytes = response_string.encode()

connection.send(response_bytes)

connection.close()
