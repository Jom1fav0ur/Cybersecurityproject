import socket

serversocket = socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999
clientsocket.connect((host, port))

message = clientsocket.recv(1024),decode()
print(message)

clientsocket.close()