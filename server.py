import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

port = 3000

server_socket.bind((host, port))
server_socket.listen(1)

while True:
	client_socket, addr = server_socket.accept()
	print("Got connection from {0}".format(addr))
	
	received_data = client_socket.recv(1024).decode("ascii")
	print("Received data from client: {0}".format(received_data))
	
	received_data = received_data.split(",")
	message = received_data[0]
	public_key = [received_data[1], received_data[2]]
	e = int(public_key[0])
	n = int(public_key[1])
	signature = int(received_data[3])
	
	print("Message is: {0}".format(message))
	print("Public Key is: {0}".format(public_key))
	print("Signature is: {0}".format(signature))
	
	m1  = pow(signature,int(e))%n
	print("M1 is: {0}".format(m1))
	
	if(m1==int(message)):
		print("Data accepted!!")
		cypher_text = pow(int(message), e)
		cypher_text = cypher_text%n
		print("Cypher text is: {0}".format(cypher_text))
		client_socket.send(str(cypher_text).encode("ascii"))
	else:
		print("Invalid data!!")

	client_socket.close()
