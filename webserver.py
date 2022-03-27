from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib


class webAPI(BaseHTTPRequestHandler):

    #    def _set_headers(self):
    #        self.send_response(200)
    #        self.send_header('Content-type', 'text/html')
    #        self.end_headers()
    #    def do_HEAD(self):
    #        self._set_headers()
    def do_GET(self):
        available_endpoints = {"/tests/database", "/tests/filesystem"}

        if self.path in available_endpoints:
            # If API endpoint is valid...
            response = "Valid question"
            self.send_response(200)
        else:
            response = "Invalid question"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(response, 'utf-8'))

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = urllib.parse.parse_qs(
            self.rfile.read(length).decode('utf-8'))
        print(post_data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("PLACEHOLDER", 'utf-8'))


def serveAPI(bind_addr, bind_port):
    ws = HTTPServer((bind_addr, bind_port), webAPI)
    try:
        ws.serve_forever()
    except KeyboardInterrupt:
        pass

    ws.server_close()
