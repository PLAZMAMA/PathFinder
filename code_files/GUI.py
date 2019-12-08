from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np

class Window(Frame):
    def __init__(self, master, width = 800, height = 800):
        super().__init__(master)
        self.master = master
        self.w = width
        self.h = height
    

    def generate_maze(self):
        """the command that is given the to button on teh gui that generates a maze to the canvas"""
        #asking the user the size of the maze they want to generate and generating the starting grid with it
        self.grid_size = simpledialog.askstring("input", "Enter the size of the maze (heightxwidth / rowsxcolumns)")
        self.grid_size = [int(self.grid_size[:self.grid_size.index("x")]), int(self.grid_size[self.grid_size.index("x") + 1:])]

        

    def get_inpt_location(self, inpt):
        """gets the given input location (only works for inputs: top-left, top-right, buttom-left, buttom-right)"""
        if inpt == "top-left":
            return([0, 0])
        elif inpt == "top-right":
            return([0, self.grid_size[1] - 1])
        elif inpt == "buttom-left":
            return([self.grid_size[0] - 1, 0])
        elif inpt == "buttom-right":
            return([self.grid_size[0] - 1, self.grid_size[1] - 1])
        else:
            return(-1)


    def find_path(self): 
        """finds the shortest path in the maze from the start to the end"""
        #getting the start and end locations until inputed correctly(from the instructions that are given in the message)
        s_inpt = simpledialog.askstring("input", "which corner of the maze would you like to start from? (top-left, top-right, buttom-left, buttom-right)")
        e_inpt = simpledialog.askstring("input", "which corner of the maze would you like to end at? (top-left, top-right, buttom-left, buttom-right)")
        s = self.get_inpt_location(s_inpt)
        e = self.get_inpt_location(e_inpt)
        while s == -1 and e == -1:
            messagebox.showerror("error", "wrong input was given")
            s_inpt = simpledialog.askstring("input", "which corner of the maze would you like to start from? (top-left, top-right, buttom-left, buttom-right)")
            e_inpt = simpledialog.askstring("input", "which corner of the maze would you like to end at? (top-left, top-right, buttom-left, buttom-right)")
            s = self.get_inpt_location(s_inpt)
            e = self.get_inpt_location(e_inpt)
        


       
            

    def display_array(self, array):
        """displayes a given array on the canvas"""
        array = np.array(array, np.uint8) #coverts the array dtype to uint8 for the image
        img = Image.fromarray(array) #converts the array into an image
        img = ImageTk.PhotoImage(img.resize((int(self.canvas.winfo_width() / 1.025), int(self.canvas.winfo_height() / 1.025)))) #resizes the image and converts it to a image that the canvas can recognize
        
        self.canvas.create_image(int(self.canvas.winfo_width()/2), int(self.canvas.winfo_height()/2), image = img) #creates the canvas image
        self.canvas.image = img #puts it on the canvas
        

    def set_win(self):
        """generates everything that is desplayed on the window and the functions of them"""

        #setting up the intial window
        self.master.title("Path Finder")
        self.master.geometry(f"{self.w}x{self.h}")

        #initializing the wigets
        self.canvas = Canvas(self.master, width = self.w - int(self.w / 50), height = self.h - int(self.h / 4), bg = "#190033")
        generate_maze = Button(self.master, text = "Generate Maze", command = self.generate_maze)
        find_path = Button(self.master, text = "Find Path", command = self.find_path, height = int(self.h / 100), width = int(self.w / 50))
        
        #placing and updating widgets to get their dimentions which are used for later placement
        find_path.place(x = 0, y = 0)
        find_path.update()
        self.canvas.place(x = 0, y = 0)
        self.canvas.update()

        #placing the widgets
        self.canvas.place(x = int(self.w/100), y = int(self.h / 5))
        generate_maze.place(x = int(self.w / 50) , y = int(self.h / 50))
        find_path.place(x = int(self.w / 2) - int(find_path.winfo_width() / 2), y = int(self.h / 50))
        
