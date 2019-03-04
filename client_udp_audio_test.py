import socket
import threading

BUFFER_SIZE = 1024
connection = ('127.0.0.1', 8080)
DATA = ''

def connect(data):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSocket.sendto(data, connection)
    msgFromServer = clientSocket.recvfrom(BUFFER_SIZE)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
        

def inputData():
    number = raw_input("Give a number:")
    while number != 0:
        print('Numer typed: ', number)
        DATA = number
        number = raw_input("Give a number:")


thread_1 = threading.Thread(name='Connection', target=connect(DATA))
thread_2 = threading.Thread(name='Entry Data', target=inputData)

thread_1.start()
thread_2.start()