import socket

ip = "192.168.215.94"
port = 4444

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip,port)
    sock.connect(address)
    
    msg = sock.rrecv(1024)
    
    print(msg.decode())
    
    sock.close()
    
main()     