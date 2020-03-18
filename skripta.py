import socket

client_socket = socket.socket()
host_name = 'www.google.com'
port = 80

client_socket.connect((host_name,port))
print ('Povezano')

client_socket.close()
