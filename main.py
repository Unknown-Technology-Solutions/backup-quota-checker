#!/usr/bin/python3
from webserver import serveAPI
from sys import argv

try:
    if type(argv[1]) is str and type(int(argv[2])) is int:
        bind_addr, bind_port = argv[1], int(argv[2])
    else:
        bind_addr, bind_port = '0.0.0.0', 8080
except:
    bind_addr, bind_port = '0.0.0.0', 8080

serveAPI(bind_addr, bind_port)
