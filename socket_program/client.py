import socket
hostname="khyaathipython"
port=1036
s=socket.socket()
try:
	s.connect((hostname,port))
	ack=s.recv(1024)
	print(ack)
	s.send(b"13er")
	resp = s.recv(1024)
	print(resp)
except Exception as err:
	print(err)
finally:
	s.close()