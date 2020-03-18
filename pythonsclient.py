import socket

client_socket = socket.socket()
host = socket.gethostname()
port = 9998

client_socket.connect((host,port))
print client_socket.recv(1099)

client_socket.close()
