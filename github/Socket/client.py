import socket

HOST = "127.0.0.1"
PORT = 65432  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b"Hello, world.... sent by client")

data = s.recv(1024)
print(f"Received {data!r}")

 
