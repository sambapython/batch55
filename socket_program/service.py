'''
hostname,port
form url
wait for the client request
accept the request if the client sends a request, and send an acknowledgement
process the request
send the response to the client
'''
import threading
def process(client_socket):
		client_socket.send(b"hello firefox how are you!!")
		req=client_socket.recv(1024)
		if req.isdigit():
			resp=b"YES"
		else:
			resp=b"NO"
		client_socket.send(resp)
import socket
hostname=socket.gethostname()
port=1036
s=socket.socket()
try:
	s.bind((hostname,port))
	s.listen(20)
	while True:
		print("waiting for the client request..")
		client_socket,client_info = s.accept()
		t=threading.Thread(target=process,args=(client_socket,))
		#process(client_socket)
		t.start()
		
except Exception as err:
	print(err)
except:
	print("some system issue")
finally:
	s.close()