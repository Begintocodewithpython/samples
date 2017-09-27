# EG15-04 Full Python web page server

import http.server

host_socket = 8080
host_ip = 'localhost'

host_address = (host_ip, host_socket)

my_server = http.server.HTTPServer(host_address,
                                   http.server.SimpleHTTPRequestHandler)
my_server.serve_forever()
