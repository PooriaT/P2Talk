import socket
import threading

################################
# Establishing Client connection
################################
def clientNodeConnectrion(host, port, username):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (host, port)

    print('Waiting for connection response')
    try:
        clientSocket.connect(address)
    except socket.error as e:
        print(str(e))

    #This the first message which is sent to server to mention its username
    username = sendUsername(clientSocket, username)

    while True:
        # #clientSocket.send(str.encode(frontClient))
        # clientSocket.send(str.encode(message))


        res = clientSocket.recv(1024)
        print(res.decode('utf-8'))
        frontClient = ''
        while frontClient == '':
            frontClient = input("To Whom you want send a message: ")
        Input = ''
        while Input == '':
            # The while loop is for inserting at least one character
            Input = input(f'Hey {username}, say something: ')

        message = '@' + frontClient + ':' + Input
        clientSocket.send(str.encode(message))


    clientSocket.close()

################################
# Sending Username to the server
################################
def sendUsername(client_S, user):
    '''
    This function sends a desired username to the server. If the username is taked,
    the client should send another one.
    '''
    status = True
    while status:
        client_S.send(str.encode(user))
        status = client_S.recv(1024)
        status = status.decode('utf-8')
        if status == 'True':
            user = input('The username has been taken. Enter another one: ')
        else:
            break
    return user





#*****************************************************
################################
# Main route
################################
if __name__=='__main__':
    host = '127.0.0.1'
    port = 2004
    username = input('Enter Your name: ')
    clientNodeConnectrion(host, port, username)
