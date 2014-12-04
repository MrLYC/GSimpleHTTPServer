#!/usr/bin/env python
# encoding: utf-8

from gevent import monkey

monkey.patch_all()

import SimpleHTTPServer
import SocketServer

__author__ = 'Liu Yicong'
__email__ = 'saber000@vip.qq.com'


def serve_forever(port):
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", port), handler)
    print "[+] serving at port", port
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "[+] GSimpleHTTPServer exited"


if __name__ == "__main__":
    import sys

    port = 8000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    serve_forever(port)
