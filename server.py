import socket
#import os
import threading
import re

################################
# Establishing Sever connections
################################
def serverNodeConnection(host, port):
	'''
	In this function a Server side connection is established and it is listening
	to any client for
	'''
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	address = (host, port)

	ThreadCount = 0

	serverSocket.bind(address)
	print('Socket is listening..')
	serverSocket.listen(5)

	connectionDic = {}
	while True:
		#Accepting Client Connection
		clientConn, clinetAddr = serverSocket.accept()
		print('Connected to: ', clinetAddr)

		#Getting the client user name:
		status = True
		while status:
			status, username = takeUsername(clientConn, connectionDic)
		connectionDic[username] = clientConn
		print(connectionDic)

		#Concurrency in order to accepting several clients' connection
		multiThreadClient = threading.Thread(target=multi_threaded_client, args=(clientConn, username ,connectionDic))
		multiThreadClient.start()



		ThreadCount += 1
		print('Thread Number: ' + str(ThreadCount))
	serverSocket.close()

################################
# Sending message to client
################################
def multi_threaded_client(connection, user, connDic):
	connection.send(str.encode('Server is working...'))
	while True:
		data = connection.recv(2048)
		print(data)
		frontUSer = re.findall(r'^@(\w+):', data.decode('utf-8'))[0]
		print(frontUSer)
		response = f'\nmessage from {user}: ' + re.findall(r'^@\w+:([\w\s]+)', data.decode('utf-8'))[0]
		if not data:
			break

		connection.sendall(str.encode(' '))
		if frontUSer == 'all':
			for name, conn in connDic.items():
				if conn != connection:
					conn.sendall(str.encode(response))
		else:
			for name, conn in connDic.items():
				if name == str.encode(frontUSer):
					conn.sendall(str.encode(response))


	connection.close()


################################
# Taking the username of clients
################################
def takeUsername(connection, connDic):
	username = connection.recv(2048) #Receving username
	for key in connDic.keys():
		if username == key:
			# Here True means, the username has been previosuly taken
			connection.send(str.encode('True'))
			return True, ''

	connection.send(str.encode('False'))
	return False, username


#*****************************************************
################################
# Main route
################################
if __name__ == '__main__':
	host = '0.0.0.0'
	port = 2004
	serverNodeConnection(host, port)
