from unittest import TestCase
from Queue import Queue

class QueueTest(TestCase):
    def setUp(self):
        self.queue = Queue()
    
    def test_add(self):
        """tests the add function"""
        self.queue.add(1)
        self.assertEqual([1], self.queue.queue)
    
    def test_remove(self):
        """tests the remove function"""
        a = self.queue.queue[0]
        self.assertEqual(a, self.queue.remove())
