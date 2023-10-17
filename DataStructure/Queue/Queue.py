from Exceptions import EmptyQueueException

class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, element):
        self.items.append(element)
        return True
    
    def front(self):
        if self.is_empty():
            raise EmptyQueueException()
        return self.items[0]
    
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueException()
        return self.items.pop(0)
