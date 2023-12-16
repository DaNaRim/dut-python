from http.server import HTTPServer, BaseHTTPRequestHandler


def do_PUT(self):
    print("PUT request received!")
    print(self.rfile.read(int(self.headers['Content-Length'])))
    self.send_response(200)
    self.end_headers()


server_class = HTTPServer
handler_class = BaseHTTPRequestHandler

server_address = ('', 8000)
httpd = server_class(server_address, handler_class)
handler_class.do_PUT = do_PUT

print("Server is running!")
httpd.serve_forever()
