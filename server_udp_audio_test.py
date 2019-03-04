import socket
import threading

port = 8080
BUFFER_SIZE = 1024
frames = []

def waitConnection():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(("", port))

    print('The server is ready to receive')

    while 1:
        data, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
        frames.append(data)
        print('Data received')
        serverSocket.sendto('Receiving data', clientAddress)
        print(len(frames))


def checkLenght():
    if len(frames) > 10:
        print('Data is complete')

thread_1 = threading.Thread(name='Connection', target=waitConnection)
thread_2 = threading.Thread(name='Checking Lenght', target=checkLenght)

thread_1.start()
thread_2.start()