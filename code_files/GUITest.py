from tkinter import Tk
from GUI import Window
from unittest import TestCase

class GUITest(TestCase):
    def setup(self):
       self.root = Tk()
       self.app = Window(self.root)
       self.app.set_win()

    def test_create_grid(self):
        expected = [[10, 206, 245], [0, 0, 0], [10, 206, 245], [0, 0, 0], [10, 206, 245], 
                    [10, 206, 245], [0, 0, 0], [10, 206, 245], [0, 0, 0], [10, 206, 245],
                    [10, 206, 245], [0, 0, 0], [10, 206, 245], [0, 0, 0], [10, 206, 245]]

        self.assertEqual(expected, self.app.create_grid(6,6))