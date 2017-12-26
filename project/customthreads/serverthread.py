import threading

class ServerThread(threading.Thread):
    '''
    This class is used as a server thread to accept incoming messages for the GUI. This 
    thread should only be created once.
    '''
    def __init__(self, runnable, *shared_thread_vars):
        threading.Thread.__init__(self)
        self.runnable = runnable
        self.shared_thread_vars = shared_thread_vars

    def run(self):
        self.runnable(self.shared_thread_vars)

class SocketThread(threading.Thread):
    '''
    This thread is spawned by the ServerThread whenever it accepts a new conenction.
    '''
    def __init__(self, runnable, conn, *shared_thread_vars):
        threading.Thread.__init__(self)
        self.runnable = runnable
        self.conn = conn
        self.shared_thread_vars = shared_thread_vars

    def run(self):
        self.runnable(self.conn, self.shared_thread_vars )