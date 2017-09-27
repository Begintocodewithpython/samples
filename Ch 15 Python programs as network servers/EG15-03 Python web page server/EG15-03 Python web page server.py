# EG15-03 Python web page server

import http.server

class WebServerHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        '''
        This method is calld when the server receives
        a GET requests from the client
        It opens a file with the requested path
        and sends back the contents
        '''
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        # trim off the leading / character in the path
        file_path = self.path[1:]

        with open(file_path,'r') as input_file:
            message_text = input_file.read()

        message_bytes = message_text.encode()

        self.wfile.write(message_bytes)
        
        return

host_socket = 8080
host_ip = 'localhost'

host_address = (host_ip, host_socket)

my_server = http.server.HTTPServer(host_address, WebServerHandler)
my_server.serve_forever()
    
