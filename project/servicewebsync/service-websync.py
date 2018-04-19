import socket
import time
import datetime
import sys

sys.path.append("../")

from websync import *
from customthreads.serverthread import *
from resources import var, varloader


# TODO: Technically, this microservice doesn't need this
# TODO: What needs to happen when we handle a socket connection??
def handle_socket_connection(conn, shared_thread_vars):
    '''
    This is a runnable used by the SocketThread.
    '''
    web_sync = shared_thread_vars[0]  # TODO: What kinds of variables are stored here?
    while True:
        try:
            # Receive data stream. Won't accept data packet greater than 1024 bytes
            message = conn.recv(1024).decode()
            print "Received message: " + message
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

    # This configures how many clients the server can listen to simultaneously
    server_socket.listen(10)

    # Server Socket is created. Now listen for any connections. Upon new connections, create a socket-parser thread
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        thread = SocketThread(handle_socket_connection, conn, web_sync)
        thread.start()

# TODO: Technically, this microservice doesn't need this
def send_message(message):
    '''
    This function sends a message passed as an argument to the function to the 
    specified host and port
    '''
    try:
        host = "servicewebsync"  # as both code is running on same pc
        port = 5000  # socket server port number
        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server
        client_socket.send(message)
        client_socket.close()  # close the connection
    except  Exception as e:
        print e


def web_cron(web_sync):
    '''
    This function periodically updates the mirror's preferences to align with
    the preferences that have been set on the web server
    '''
    print var.last_updated
    while True:
        time.sleep(10) # TODO change to 10s when developing in scenarios

        # Printing the current timestamp for debugging purposes
        curr_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print curr_time

        web_sync.update_all()

    # TODO: Is the web server periodically updating itself to align with the mirror?


if __name__ == '__main__':
    web_sync = WebSync()  # TODO: Why do we pass web_sync as shared_thread_vars?
    # thread1 = ServerThread(web_sync_server, web_info, last_update_info)
    # thread1.start()
    web_cron(web_sync)
