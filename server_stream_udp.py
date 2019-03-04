import SocketServer
import threading

ServerAddress = ('127.0.0.1', 8080)

class MyUDPRequestHandler(SocketServer.DatagramRequestHandler):
    def handle(self):
        print("Recieved one request from {}".format(self.client_address[0]))
        datagram = self.rfile.readline().strip()
        print("Datagram Recieved from client is:".format(datagram))
        print(datagram)
        print("Thread Name:{}".format(threading.current_thread().name))
        self.wfile.write("Message from Server! Hello Client".encode())

UDPServerObject = SocketServer.ThreadingUDPServer(ServerAddress, MyUDPRequestHandler)
UDPServerObject.serve_forever()