# certificaat maken met openssl: "openssl req -new -x509 -keyout cert.pem -out cert.pem -days 365 -nodes"

import http.server, ssl, socketserver

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("cert.pem") 
server_address = ("10.0.100.4", 443) 

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(server_address, handler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()
