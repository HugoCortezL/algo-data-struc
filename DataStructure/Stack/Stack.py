from Exceptions import EmptyStackException

class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def push(self, element):
        self.items.append(element)
        return True
    
    def top(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.items[-1]
    
    def pop(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.items.pop()
