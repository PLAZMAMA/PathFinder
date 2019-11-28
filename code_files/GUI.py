from tkinter import *
from PIL import Image, ImageTk
import numpy as np

class Window(Frame):
    def __init__(self, master, width = 800, height = 800):
        super().__init__(master)
        self.master = master
        self.w = width
        self.h = height
    
    def create_grid(self, rows, columns):
        """
        creates a grid from the given odd rows and columns. If rows or columns are even, 
        it changes either or to the  closest smallest odd number and then returns grid array
        """
        #generates the maze with black walls in between each blue cell

        #checks if rows or columns are even and if they are, it changes them to odd
        if rows % 2 == 0:
            rows -= 1
        if columns % 2 == 0:
            columns -= 1
        #creates the output array with the corrected sizes
        output = np.zeros((rows, columns, 3), dtype = np.int32)

        #loops and creates the walls and cells(aka the grid)
        for r in range(rows):
            if r % 2 == 0:
                for c in range(columns):
                    if c % 2 == 0:
                        output[r][c] = [10, 206, 245]
                    else:
                        output[r][c] = [0, 0, 0]
            else:
                for c in range(columns):
                    output[r][c] = [0, 0, 0]

        return(output)

    def generate_maze(self):
        """generates the maze to the canvas"""
        grid = self.create_grid(100,100)
        self.display_array(grid)
        self.canvas.configure(color = "red")

   
    def find_path(self): 
        """finds the shortest path in the maze from the start to the end"""
        pass

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

        #configuring the starting grid and displaying it on the canvas
        grid = self.create_grid(100,100)
        self.display_array(grid)
        
