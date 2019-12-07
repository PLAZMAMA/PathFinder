from tkinter import Tk
from GUI import Window
from unittest import TestCase

class GUITest(TestCase):
    def setup(self):
       self.root = Tk()
       self.app = Window(self.root)
       self.app.set_win()

    def test_create_grid(self):
        """tests the create grid method of the GUI class"""
        expected = [[10, 206, 245], [0, 0, 0], [10, 206, 245], [0, 0, 0], [10, 206, 245], 
                    [10, 206, 245], [0, 0, 0], [10, 206, 245], [0, 0, 0], [10, 206, 245],
                    [10, 206, 245], [0, 0, 0], [10, 206, 245], [0, 0, 0], [10, 206, 245]]

        self.assertEqual(expected, self.app.create_grid(6,6))
    
    def test_get_inpt_location(self):
        self.app.grid_size = [9,9]
        self.assertEqual([0,0], self.app.get_inpt_location("top-left"))
        self.assertEqual([0,8], self.app.get_inpt_location("top-right"))
        self.assertEqual([8,0], self.app.get_inpt_location("buttom-left"))
        self.assertEqual([8,8], self.app.get_inpt_location("buttom-right"))