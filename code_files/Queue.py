
class Queue():
    def __init__(self):
        self.queue = []

    def add(self, n):
        """adds an number to the queue"""
        self.queue.append(n)
    
    def remove(self):
        """removes the first number from the queue and returns it"""
        return(self.queue.pop(0))

