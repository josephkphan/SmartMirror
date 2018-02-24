import socket
import time
import sys

from uihandler import *
from customthreads.serverthread import *
from datastructures.queue import *

def handle_socket_connection(conn, shared_thread_vars):
    '''
    This is a runnable used by the SocketThread. Upon accepting socket connection. It will spawn the 
    SocketThread that will run this function. This function parses all the messages through this connection
    and will add it to the respective queue for the GUI -- if valid
    '''
    direction_queue = shared_thread_vars[0]
    event_queue = shared_thread_vars[1]
    coordinate_queue = shared_thread_vars[2]
    while True:
        try:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            message = conn.recv(1024).decode()
            direction_queue.enqueue(message)

            # Checks for messages related to directions
            if 'direction_' in message:
                # NOTE: This check does not check the full string. 
                if 'right' in message or 'left' in message or 'up' in message or 'down' in message:
                    direction_queue.enqueue(message)
                else:
                    print 'Invalid Direction Message'

                    # Check for update related messages
            elif 'event_' in message:
                event_queue.enqueue(message)

            elif 'coordinate_' in message:
                coordinate_queue.enqueue(message)

            # Error handling for messages in incorrect format
            else:
                # NOTE: This will break out of the loop and result in ending the client connection
                print 'message error!: ', message
                break

                # Send an Ack for every correct response
            response = 'ack'
            conn.send(response.encode())

        # Exception Handling for anything else...
        except Exception as e:
            print e
            break
    conn.close()  # NOTE: Will only close connection from error or break


def gui_server(shared_thread_vars):
    '''
    This is the runnable used by Server Thread. It sets up the server socket. 
    Note: There is a max number of connections allowed. 
    '''
    direction_queue = shared_thread_vars[0]
    event_queue = shared_thread_vars[1]
    coordinate_queue = shared_thread_vars[2]
    # Gather Data on the machine and create the server Socket 
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))

    # This configure how many client the server can listen simultaneously
    server_socket.listen(10)

    # Server Socket is created. Now listen for any connections. Upon new connections, create a socket-parser thread
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        thread = SocketThread(handle_socket_connection, conn, direction_queue, event_queue, coordinate_queue)
        thread.start()


def gui_application(ui_manager, direction_queue, event_queue, coordinate_queue):
    '''
    This is the function that creates and update the Mirror GUI 
    Note: This function HAS to be run in the main thread (due to TKInter limitations)
    '''
    while True:
        # time.sleep(.5)
        if not event_queue.is_empty():
            print 'Update Queue: ', event_queue.to_list()
            ui_manager.update_all_manually(event_queue.dequeue())            
        elif not direction_queue.is_empty():
            print 'Direction Queue: ',direction_queue.to_list()
            ui_manager.update_all_manually(direction_queue.dequeue()) 
        else: 
            ui_manager.update_all_manually() 



if __name__ == '__main__':
    ui_manager = UIManager(True, True)
    direction_queue = Queue()
    event_queue = Queue()
    coordinate_queue = Queue()
    thread1 = ServerThread(gui_server, direction_queue, event_queue, coordinate_queue)
    thread1.start()
    gui_application(ui_manager, direction_queue, event_queue, coordinate_queue)




    # def client_message(host, port, message):
    #     host = socket.gethostname()  # as both code is running on same pc
    #     port = 5000  # socket server port number
    #     client_socket = socket.socket()  # instantiate
    #     client_socket.connect((host, port))  # connect to the server
    #     client_socket.send(message)
    #     client_socket.close()  # close the connection