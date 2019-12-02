
class Stack():
    def __init__(self):
        self.stack = []

    def add(self, n):
        """adds to the stack a given number"""
        self.stack.append(n)
    
    def remove(self):
        """removes from the stack a given element and returns"""
        return(self.stack.pop(len(self.stack) - 1))