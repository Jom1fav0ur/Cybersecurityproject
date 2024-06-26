import socket 

ip = "192.168.215.94" 
port = 4444

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip,port)
    sock.bind(address)
    sock.listen(1)
    print("listening for connection on port" + str(port))
    
    conn , ipvictim = sock.accept()
    msg = "this is the message from the server"
    conn.send(msg.encode()) 
    conn.close()
    
main()    
    