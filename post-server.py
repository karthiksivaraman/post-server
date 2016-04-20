from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import ssl 

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        print self.headers
        self.post_data = self.rfile.read(int(self.headers['Content-Length']))
        
        self.send_response(200)
        self.end_headers()

        filename = self.headers.get('X-filename', 'default') + '.gz'
        with open(filename, 'w') as fout:
            fout.write(self.post_data)

def run(server_class=HTTPServer, handler_class=Server, port=8443):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile='server.pem', server_side=True)
    print 'Starting HTTPS server at %s ...' %port
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
