
import threading

class RunnableThread(threading.Thread):
    def __init__(self, runnable):
        threading.Thread.__init__(self)
        self.runnable = runnable

    def run(self):
        self.runnable()


import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    # port = raw_input("Server port to connect: ")
    print host
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        # data = raw_input(' -> ')
        # conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection



def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5001  # socket server port number
    # port = raw_input("Server port to connect: ")
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = raw_input(" -> ")  # take input

    while True:
        try:
            result = client_socket.connect_ex((host, port))
            print result
            client_socket.send(message.encode())  # send message
            #data = client_socket.recv(1024).decode()  # receive response

            #print('Received from server: ' + data)  # show in terminal

            message = raw_input(" -> ")  # again take input
        except Exception as e:
            print 'Connection with GUI Closed'
            break

    client_socket.close()  # close the connection

if __name__ == '__main__':
    thread1 = RunnableThread(server_program)
    thread1.start()
    thread2 = RunnableThread(client_program)
    thread2.start()

