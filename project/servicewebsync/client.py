import socket

'''
This program is used to communicate with the microservice running the GUI
'''
def client_program():
    host = "servicegui"  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = raw_input(" -> ")  # take input

    while True:
        try:
            result = client_socket.connect_ex((host, port))
            print result
            client_socket.send(message.encode())  # send message
            client_socket.settimeout(1)
            data = client_socket.recv(1024).decode()  # receive response
            print('Received from server: ' + data)  # show in terminal
            if not data:
                break

            message = raw_input(" -> ")  # again take input
        except Exception as e:
            print 'Connection with GUI Closed'
            break

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()