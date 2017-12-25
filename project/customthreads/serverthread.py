import threading

class ServerThread(threading.Thread):
    '''
    This class is used as a server thread to accept incoming messages for the GUI. This 
    thread should only be created once.
    '''
    def __init__(self,  direction_queue, update_queue, runnable):
        threading.Thread.__init__(self)
        self.runnable = runnable
        self.direction_queue = direction_queue
        self.update_queue = update_queue


    def run(self):
        self.runnable(self.direction_queue, self.update_queue)

class SocketThread(threading.Thread):
    '''
    This thread is spawned by the ServerThread whenever it accepts a new conenction.
    '''
    def __init__(self, conn, direction_queue, update_queue, runnable):
        threading.Thread.__init__(self)
        self.runnable = runnable
        self.conn = conn
        self.direction_queue = direction_queue
        self.update_queue = update_queue

    def run(self):
        self.runnable(self.conn, self.direction_queue, self.update_queue )