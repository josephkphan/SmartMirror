import socket
import time
import sys

sys.path.append("../")

from project.serviceweb.webinfo import *
from project.customthreads.serverthread import *
from project.resources import var, varloader


def handle_socket_connection(conn, shared_thread_vars):
    '''
    This is a runnable used by the SocketThread. Upon accepting socket connection. It will spawn the 
    SocketThread that will run this function. This function parses all the messages through this connection
    and will add it to the respective queue for the GUI -- if valid
    '''
    web_info = shared_thread_vars[0]
    last_update_info = shared_thread_vars[1]
    while True:
        try:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            message = conn.recv(1024).decode()

            # Checks for messages related to directions
            if 'event_update_now' in message:
                print 'doing update'
                web_info.thread_update()
                web_data_updated_message('event_updating_data')
                # Do the update!

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


def web_info_server(shared_thread_vars):
    '''
    This is the runnable used by Server Thread. It sets up the server socket. 
    Note: There is a max number of connections allowed. 
    '''
    web_info = shared_thread_vars[0]
    last_update_info = shared_thread_vars[1]
    # Gather Data on the machine and create the server Socket 
    host = socket.gethostname()
    port = 5001
    server_socket = socket.socket()
    server_socket.bind((host, port))

    # This configure how many client the server can listen simultaneously
    server_socket.listen(10)

    # Server Socket is created. Now listen for any connections. Upon new connections, create a socket-parser thread
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        thread = SocketThread(handle_socket_connection, conn, web_info, last_update_info)
        thread.start()


def web_cron(web_info, last_update_info):
    '''
    This is the function that creates and update the Mirror GUI 
    Note: This function HAS to be run in the main thread (due to TKInter limitations)
    '''
    print var.last_updated
    while True:
        if var.is_updating and var.update_completed:
            print 'Sending Finish Message to GUI'
            #TODO: Send client message ... What happens if it fails??
            web_data_updated_message('event_updated_now')
            var.is_updating = False
            var.update_completed = False
        
        if not var.is_updating:
            last_update_time = (time.time() - var.last_updated) / 60
            print last_update_time, ' -- ', var.update_time
            if last_update_time >= var.update_time:
                print 'update now'
                web_info.thread_update()
                web_data_updated_message('event_updating_data')
            else:
                time.sleep(.5)
        # Check if last update Info >10min AND if it is currently updating or not
        # ping GUI application that update is complete


if __name__ == '__main__':
    web_info = WebInfo()
    last_update_info = {}
    # TODO: Find out when it was last updated
    # TODO: have a boolean whether it is currently updating.. don't DDOS yourself
    thread1 = ServerThread(web_info_server, web_info, last_update_info)
    thread1.start()
    web_cron(web_info, last_update_info)



def web_data_updated_message(message):
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    client_socket.send(message)
    client_socket.close()  # close the connection


