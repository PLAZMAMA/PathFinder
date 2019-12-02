from unittest import TestCase
from Stack import Stack

class StackTest(TestCase):
    def setUp(self):
        self.stack = Stack()
    
    def test_add(self):
        """tests the add method in Stack"""
        self.stack.add(1)
        self.assertEqual([1], self.stack.stack)
    
    def test_remove(self):
        """tests the remove method in Stack"""
        self.stack.stack = [2, 3, 1, 6, 9]
        self.stack.remove()
        self.assertEqual([2, 3, 1, 6], self.stack.stack)