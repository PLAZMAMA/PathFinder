from tkinter import *

class Window(Frame):
    def __init__(self, master, width = 800, height = 800):
        super().__init__(master)
        self.master = master
        self.w = width
        self.h = height
    

    def generate_maze(self):
        pass
    
    def find_path(self):
        pass

    def set_win(self):
        #setting up the intial window
        self.master.title("Path Finder")
        self.master.geometry(f"{self.w}x{self.h}")

        #initializing the wigets
        canvas = Canvas(self.master, width = self.w - int(self.w / 50), height = self.h - int(self.h / 4), bg = "blue")
        generate_maze = Button(self.master, text = "Generate Maze", command = self.generate_maze)
        find_path = Button(self.master, text = "Find Path", command = self.find_path, height = int(self.h / 100), width = int(self.w / 50))
        
        #placing and updating widgets to get their dimentions which are used for later placement
        find_path.place(x = 0, y = 0)
        find_path.update()

        #placing the widgets
        canvas.place(x = int(self.w/100), y = int(self.h / 5))
        generate_maze.place(x = int(self.w / 50) , y = int(self.h / 50))
        find_path.place(x = int(self.w / 2) - int(find_path.winfo_width() / 2), y = int(self.h / 50))
        
