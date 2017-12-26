import threading

class GuiServerThread(threading.Thread):
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

class GuiSocketThread(threading.Thread):
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


#--------------------------------------------------------------------------------------- #

class WebServerThread(threading.Thread):
    '''
    This class is used as a server thread to accept incoming messages for the GUI. This 
    thread should only be created once.
    '''
    def __init__(self, web_info, last_update_info, runnable):
        threading.Thread.__init__(self)
        self.runnable = runnable
        self.last_update_info = last_update_info
        self.web_info = web_info


    def run(self):
        self.runnable(self.web_info, self.last_update_info)

class WebSocketThread(threading.Thread):
    '''
    This thread is spawned by the ServerThread whenever it accepts a new conenction.
    '''
    def __init__(self, conn, web_info, last_update_info, runnable):
        threading.Thread.__init__(self)
        self.runnable = runnable
        self.conn = conn
        self.last_update_info = last_update_info
        self.web_info = web_info

    def run(self):
        self.runnable(self.conn, self.web_info,  self.last_update_info )
