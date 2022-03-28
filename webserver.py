from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import urllib
import api_outputs as apio

class webAPI(BaseHTTPRequestHandler):

    #    def _set_headers(self):
    #        self.send_response(200)
    #        self.send_header('Content-type', 'text/html')
    #        self.end_headers()
    #    def do_HEAD(self):
    #        self._set_headers()
    def do_GET(self):

        if self.path in apio.available_endpoints:
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

class threadHTTPServ(ThreadingMixIn, HTTPServer):
    """
    Handle requests in a seperate thread
    """
    pass

def serveAPI(bind_addr, bind_port):
    ws = threadHTTPServ((bind_addr, bind_port), webAPI)
    ws.serve_forever()
#    try:
#        ws.serve_forever()
#    except KeyboardInterrupt:
#        pass

    ws.server_close()
