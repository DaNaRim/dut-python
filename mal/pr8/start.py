from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print("Server is running! Available links:")
print("http://localhost:8000/index.html")
print("http://localhost:8000/cgi-bin/cookie.py")
print("http://localhost:8000/cgi-bin/wall.py")
httpd.serve_forever()
