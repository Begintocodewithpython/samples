# EG15-02 Python web server

import http.server

class webServerHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        '''
        This method is called when the server receives
        a GET requests from the client
        It sends a fixed message back to the client
        '''
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message_text = '''<html>
<body>
<p>hello from the Python server</p>
</body>
</html>
'''
        message_bytes = message_text.encode()

        self.wfile.write(message_bytes)
        return

host_socket = 8080
host_ip = 'localhost'

host_address = (host_ip, host_socket)

my_server = http.server.HTTPServer(host_address, webServerHandler)
my_server.serve_forever()
    
