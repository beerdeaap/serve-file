#!/usr/bin/python
"""
Serves one file over HTTP on a certain port (whatever the request).
Mimetype will be guessed using the `mimetype` lib.

Usage: ./serve.py filename.xml 8776
"""

import BaseHTTPServer
import mimetypes
import sys


def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    @property
    def mimetype(self):
        mimetype, _ = mimetypes.guess_type(filename, strict=False)
        return mimetype or 'text/html'

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", self.mimetype)
        self.end_headers()

    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", self.mimetype)
        self.end_headers()

        with open(filename, "rb") as file_:
            self.wfile.write(file_.read())
            file_.close()

    def do_POST(self):
        return self.do_GET()

    def do_PUT(self):
        return self.do_GET()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: <path> <port>\n")
        sys.exit(1)

    filename = sys.argv[1]
    port = int(sys.argv[2])

    run(handler_class=Handler)
