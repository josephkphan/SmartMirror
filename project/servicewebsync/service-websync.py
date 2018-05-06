import socket
import time
import datetime
import sys

sys.path.append("../")

from websync import *
from customthreads.serverthread import *
from resources import var, varloader


def handle_socket_connection(conn, shared_thread_vars):
    '''
    This is a runnable used by the SocketThread. Upon accepting socket connection
    SocketThread will run this function. This function parses and handles
    incoming messages.
    '''
    web_sync = shared_thread_vars[0]
    
    while True:
        try:
            # Receive data stream (won't accept data packet > 1024 bytes)
            message = conn.recv(1024).decode()
            print 'Message Received: ',message
            web_sync.send_updates()

            # Send an Ack for every correct response
            response = 'ack'
            conn.send(response.encode())

        # Exception Handling for anything else...
        except Exception as e:
            print e
            break

    conn.close()  # NOTE: Will only close connection from error or break


def web_sync_server(shared_thread_vars):
    '''
    This is the runnable used by Server Thread. It sets up the server socket. 
    Note: There is a max number of connections allowed. 
    '''
    web_sync = shared_thread_vars[0]

    # Gather Data on the machine and create the server Socket 
    host = socket.gethostname()
    port = 5002
    server_socket = socket.socket()
    server_socket.bind((host, port))

    # This configure how many client the server can listen simultaneously
    server_socket.listen(10)

    # Server Socket is created. Now listen for any connections. Upon new connections, create a socket-parser thread
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        thread = SocketThread(handle_socket_connection, conn, web_sync)
        thread.start()


def web_cron(web_sync):
    '''
    This function periodically updates the mirror's preferences to align with
    the preferences that have been set on the web server
    '''
    print var.last_updated
    while True:
        time.sleep(10)

        # Printing the current timestamp for debugging purposes
        curr_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print curr_time

        web_sync.update_all()


if __name__ == '__main__':
    web_sync = WebSync()

    # Separate thread used to handle incoming messages
    thread1 = ServerThread(web_sync_server, web_sync)
    thread1.start()

    # Main thread executes our cronjob
    web_cron(web_sync)
