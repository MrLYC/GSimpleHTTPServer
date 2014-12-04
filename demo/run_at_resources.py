#!/usr/bin/env python
# encoding: utf-8

from GSimpleHTTPServer import serve_forever
import sys
import os
from os import path

port = 8000
if len(sys.argv) > 1:
    port = int(sys.argv[1])

selfpath = path.realpath(path.dirname(__file__))
rootdir = path.join(selfpath, "resources")
os.chdir(rootdir)
print "[+] change directory to", rootdir

serve_forever(port)
