import http.server
import socketserver

PORT = 7777
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port http://localhost:"+str(PORT)+"/")
    httpd.serve_forever()