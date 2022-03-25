from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class webAPI(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            # If API endpoint is valid...
            response = "Valid question"
            self.send_response(200)
        except:
            response = "Invalid question"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(response, 'utf-8'))

def serveAPI(bind_addr, bind_port):
    ws = HTTPServer((bind_addr, bind_port), webAPI)
    try:
        ws.serve_forever()
    except KeyboardInterrupt:
        pass
    
    ws.server_close()