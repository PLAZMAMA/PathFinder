from tkinter import Tk
from GUI import Window
from unittest import TestCase

class GUITest(TestCase):
    def setup(self):
       self.root = Tk()
       self.app = Window(self.root)
       self.app.set_win()
    
    def test_get_inpt_location(self):
        self.app.grid_size = [9,9]
        self.assertEqual([0,0], self.app.get_inpt_location("top-left"))
        self.assertEqual([0,8], self.app.get_inpt_location("top-right"))
        self.assertEqual([8,0], self.app.get_inpt_location("buttom-left"))
        self.assertEqual([8,8], self.app.get_inpt_location("buttom-right"))