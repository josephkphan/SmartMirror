import socket
import time
import sys

sys.path.append("../")

from project.serviceweb.webinfo import *
from project.customthreads.serverthread import *
from project.servicecamera.camera import *


def handle_socket_connection(conn, shared_thread_vars):
    '''
    This is a runnable used by the SocketThread. Upon accepting socket connection. It will spawn the 
    SocketThread that will run this function. This function parses all the messages through this connection
    and will add it to the respective queue for the GUI -- if valid
    '''
    camera  = shared_thread_vars[0]
    camera_mode = shared_thread_vars[1]
    while True:
        try:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            message = conn.recv(1024).decode()

            # TODO: Handle case to handle Power Off Camera??
            print message

            # Send an Ack for every correct response
            response = 'ack'
            conn.send(response.encode())

        # Exception Handling for anything else...
        except Exception as e:
            print e
            break
    conn.close()  # NOTE: Will only close connection from error or break


def camera_server(shared_thread_vars):
    '''
    This is the runnable used by Server Thread. It sets up the server socket. 
    Note: There is a max number of connections allowed. 
    '''
    camera  = shared_thread_vars[0]
    camera_mode = shared_thread_vars[1]
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
        thread = SocketThread(handle_socket_connection, conn, camera, camera_mode)
        thread.start()


def camera_cron(camera, camera_mode):
    '''
    This is the function that creates and update the Mirror GUI 
    Note: This function HAS to be run in the main thread (due to TKInter limitations)
    '''
    while True:
        camera.turn_on()
        camera.update_values()
        cursor_location = camera.get_cursor()
        print cursor_location
        k = cv2.waitKey(10)
        if k == 27:  # Esc key breaks out of program
            exit()             # break out of program
        #time.sleep(.5)



if __name__ == '__main__':
    camera = Camera(var.wall_light_color)
    camera_mode = {}
    thread1 = ServerThread(camera_server, camera, camera_mode)
    thread1.start()
    camera_cron(camera, camera_mode)



def web_data_updated_message(message):
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    client_socket.send(message)
    client_socket.close()  # close the connection


