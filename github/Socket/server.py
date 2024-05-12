import socket			 

HOST = "127.0.0.1"  
PORT = 65432  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		

s.bind((HOST, PORT))
s.listen()

	 
print ("socket binded to %s" %(PORT)) 

print ("socket is listening....")		 

 
while True: 

    con, addr = s.accept()	 
    print ('Got connection from', addr )

    con.send(b"Thank you for connecting...sent by server")
    data = con.recv(1024) 
    print(f"Received {data!r}")

    con.close()
    break

