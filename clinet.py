import socket
import threading
from cryptography.fernet import Fernet


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
        # Defining Cryptography protocol with available key
        f = Fernet(symKeyEnc)

        Input = ''
        while Input == '':
            # The while loop is for inserting at least one character
            Input = input(f'Hey {username}: ')
            
        clientSocket.send(f.encrypt(str.encode(Input)))
        res = clientSocket.recv(1024)
        res = f.decrypt(res)
        print(res.decode('utf-8'))


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
    #Defining the generated key by the server for encryption messages
    global symKeyEnc
    with open('SKE.txt', 'rb') as file:
        symKeyEnc = file.read()

    #Defining host and port
    host = '127.0.0.1'
    port = 2004
    username = input('Enter Your name: ')
    clientNodeConnectrion(host, port, username)
