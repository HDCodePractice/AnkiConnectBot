from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

keyfile = "../127.0.0.1-key.pem"
certfile = '../127.0.0.1.pem'
hostname = 'localhost'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certfile, keyfile=keyfile)

httpd = HTTPServer((hostname, 4443), SimpleHTTPRequestHandler)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()
