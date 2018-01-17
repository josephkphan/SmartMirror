class Queue:
    '''
    This class is used as the shared object between threads. The server thread will write into queues
    and then the GUI application will read commands from queues
    NOTE: Should there some locks when enqueue / dequeue??? potential race conditions?? 
    '''
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def to_list(self):
        return self.items