import socket
import threading
import schedule
import time
import sys

sys.path.append("../")

from project.uimanagers.webinfo import *
from project.customthreads.serverthread import *
from project.datastructures.queue import *


def handle_socket_connection(conn, web_info, last_update_info):
    '''
    This is a runnable used by the SocketThread. Upon accepting socket connection. It will spawn the 
    SocketThread that will run this function. This function parses all the messages through this connection
    and will add it to the respective queue for the GUI -- if valid
    '''
    while True:
        try:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            message = conn.recv(1024).decode()

            # Checks for messages related to directions
            if 'event_update_now' in message:
                print 'doing update'
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


def web_info_server(web_info, last_update_info):
    '''
    This is the runnable used by Server Thread. It sets up the server socket. 
    Note: There is a max number of connections allowed. 
    '''

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
        thread = WebSocketThread(conn, web_info, last_update_info, handle_socket_connection)
        thread.start()


def web_cron(web_info, last_update_info):
    '''
    This is the function that creates and update the Mirror GUI 
    Note: This function HAS to be run in the main thread (due to TKInter limitations)
    '''
    while True:
        time.sleep(.5)
        # Check if last update Info >10min AND if it is currently updating or not
        # ping GUI application that update is complete


if __name__ == '__main__':
    web_info = WebInfo()
    last_update_info = {}
    # TODO: Find out when it was last updated
    # TODO: have a boolean whether it is currently updating.. don't DDOS yourself
    thread1 = WebServerThread(web_info, last_update_info, web_info_server)
    thread1.start()
    web_cron(web_info, last_update_info)



def web_data_updated_message(host, port, message):
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    client_socket.send(message)
    client_socket.close()  # close the connection



    # ---------------------------------- Web Info Updating Functions ----------------------------------- #
def update_web_info(self):
    last_update_time = (time.time() - var.last_updated) / 60
    # print last_update_time
    if last_update_time >= var.update_time and self.current_page == Page.main:  # todo only update on main page??
        # Means its been 10 minutes since it last updated
        # print "UPDATING WEB INFO. REQUESTING FROM WEB"
        self.main_clock.change_update_label_to_updating()
        self.web_info_update()

def web_info_update(self):
    self.web_info.thread_update()

def check_if_web_info_update_thread_is_complete(self):
    if var.is_updating and var.update_completed:

        self.update_all_widgets_content()
        var.is_updating = False
        var.update_completed = False


def on_startup(self):
    # Setting initial zone and page data
    last_update_time = (time.time() - var.last_updated) / 60
    # print last_update_time
    if not(last_update_time >= var.update_time and self.current_page == Page.main):
        time.sleep(3)
    else:
        self.web_info_update()
        self.update_all_widgets_content()


