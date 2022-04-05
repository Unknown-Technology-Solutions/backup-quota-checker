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
            self.send_response(200)
            response = apio.handle_endpoint(self.path, apio.fsdb.dg.auth_to_db(
                "infoMan", "placeholder"), None, "get")
        else:
            self.send_response(404)
            response = '{"error": "CEC601"}'
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(response, 'utf-8'))

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        # print(post_data.decode())
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
#        response = apio.read_usage_data(apio.fsdb.dg.auth_to_db("infoMan", "placeholder"), post_data)
        response = apio.handle_endpoint(self.path, apio.fsdb.dg.auth_to_db(
            "infoMan", "placeholder"), post_data, "post")
        self.wfile.write(bytes(response, 'utf-8'))


class threadHTTPServ(ThreadingMixIn, HTTPServer):
    """
    Handle requests in a seperate thread
    """
    pass


def serveAPI(bind_addr, bind_port):
    print("Serving on " + bind_addr + ":" + str(bind_port))
    ws = threadHTTPServ((bind_addr, bind_port), webAPI)
    ws.serve_forever()
#    try:
#        ws.serve_forever()
#    except KeyboardInterrupt:
#        pass

    ws.server_close()
