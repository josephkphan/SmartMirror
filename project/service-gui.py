import socket
import threading


class SocketThread(threading.Thread):
    def __init__(self, conn, runnable):
        threading.Thread.__init__(self)
        self.runnable = runnable
        self.conn = conn


    def run(self):
        self.runnable(self.conn)

def handle_socket_connection(conn):
    while True:
        try:
            #conn.settimeout(5)
            message = conn.recv(1024).decode()         # receive data stream. it won't accept data packet greater than 1024 bytes
            if message == 'left':
                print 'left'
            elif message == 'up':
                print 'up'
            elif message == 'down':
                print 'down'
            elif message == 'right':
                print 'right'
            elif message == 'data updated':
                print 'data updated'
            elif message == 'data updated':
                print 'data updated'
            else:
                print 'message error!: ', message
                break;
            
            response='ack'
            # conn.send(response.encode())
        except Exception as e:
            print e
            break
    conn.close()  # close the connection

def gui_server():
    host = socket.gethostname()  # get the hostname
    port = 5000  # initiate port no above 1024

    print host
    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together
    server_socket.listen(10)  # configure how many client the server can listen simultaneously

    
   
    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        thread = SocketThread(conn,handle_socket_connection)
        thread.start()
        
        



def client_message(host,port,message):
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    client_socket.send(message)
    client_socket.close()  # close the connection


if __name__ == '__main__':
    gui_server()