from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import random
from Stack import Stack
from Queue import Queue

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
        #asking the user the size of the maze they want to generate and generating the starting grid with it
        self.grid_size = simpledialog.askstring("input", "Enter the size of the maze (heightxwidth / rowsxcolumns)")
        self.grid_size = [int(self.grid_size[:self.grid_size.index("x")]), int(self.grid_size[self.grid_size.index("x") + 1:])]

        #checks if rows or columns are even and if they are, it changes them to odd
        if self.grid_size[0] % 2 == 0:
            self.grid_size[0] -= 1
        if self.grid_size[1] % 2 == 0:
            self.grid_size[1] -= 1

        self.grid = self.create_grid(self.grid_size[0], self.grid_size[1])
        self.display_array(self.grid) #displaying the grid

        #creating two stacks. One for columns and on for rows coordinates
        c_stack = Stack()
        r_stack = Stack()

        #created a visited list, initializing the starting node, marking it True(aka visited) and adding its coordinates to each of the stacks
        visited = np.zeros((self.grid_size[0], self.grid_size[1]), dtype = np.bool)
        c = 0
        r = 0
        visited[r][c] = True
        c_stack.add(c)
        r_stack.add(r)

        #starting with the starting node, then cheking its neighbors, if there are any choosing one at random.
        #If there are not, backtraking to a node that has neightbors. (this will end once it backtracks to the starting now aka when the stack is empty)
        while len(c_stack.stack) >= 0:

            #creating the neighbors list and adding the neightbors of the node to it
            neighbors = []
            if c + 2 < self.grid_size[1] and visited[r][c + 2] == False:
                neighbors.append("right")
            if c - 2 > 0 and visited[r][c - 2] == False:
                neighbors.append("left")
            if r - 2 > 0 and visited[r - 2][c] == False:
                neighbors.append("up")
            if r + 2 < self.grid_size[0] and visited[r + 2][c] == False:
                neighbors.append("down")

            # choosing a neighbor at random if there are any neighbors, displaying it, adding the coordinates to the stack, making the current node's locaions right
            if len(neighbors) > 0:
                choice = random.choice(neighbors)
                if choice == "right":
                    self.grid[r][c + 1] = [10, 206, 245]
                    self.display_array(self.grid)
                    c += 2
                    visited[r][c] = True
                    c_stack.add(c)
                    r_stack.add(r)
                elif choice == "left":
                    self.grid[r][c - 1] = [10, 206, 245]
                    self.display_array(self.grid)
                    c -= 2
                    visited[r][c] = True
                    c_stack.add(c)
                    r_stack.add(r)
                elif choice == "up":
                    self.grid[r - 1][c] = [10, 206, 245]
                    self.display_array(self.grid)
                    r -= 2
                    visited[r][c] = True
                    c_stack.add(c)
                    r_stack.add(r)
                else:
                    self.grid[r + 1][c] = [10, 206, 245]
                    self.display_array(self.grid)
                    r += 2
                    visited[r][c] = True
                    c_stack.add(c)
                    r_stack.add(r)
            
            #if there are no elements in the stack
            elif len(c_stack.stack) == 0:
                break
            
            #if there are not neighbors
            else:
                c = c_stack.remove()
                r = r_stack.remove()

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


        #initializing the queues
        rq = Queue()
        cq = Queue()

        #initially marking reached end as false (used to know if the end is reachable)
        reached_end = False

        #initializing the visited array to keep track of visited nodes and a prev array to keep track of the path
        visited = np.zeros((self.grid_size[0], self.grid_size[1]), dtype = np.bool)
        prev = []
        for i in range(self.grid_size[0]):
	        prev.append([])
	        for _ in range(self.grid_size[1]):
		        prev[i].append([None, None])
        
        #added the starting row position to the row queue and starting column position to the column queue
        rq.add(s[0])
        cq.add(s[1])

        #marked the first positions as true
        visited[s[0]][s[1]] = True

        #running while the queues is not empty (only put one because the queue will always be the same size)
        while len(cq.queue) > 0:
            #removes the nodes coordinates from the queues and puts them into the variables r, c
            r = rq.remove()
            c = cq.remove()

            #checks if the node location is the same as the end location (checks if it reached the end)
            if r == e[0] and c == e[1]:
                reached_end = True
                break
            
            #adding to it the appropriate neighbors to the queues and the visited and prev arrays
            if c + 2 < self.grid_size[1] and np.all(self.grid[r][c + 1] == [10, 206, 245]) and visited[r][c + 2] == False:
                rq.add(r)
                cq.add(c + 2)
                visited[r][c + 2] = True
                prev[r][c + 1][0] = r
                prev[r][c + 1][1] = c
                prev[r][c + 2][0] = r
                prev[r][c + 2][1] = c + 1
            if c - 2 >= 0 and np.all(self.grid[r][c - 1] == [10, 206, 245]) and visited[r][c - 2] == False:
                rq.add(r)
                cq.add(c - 2)
                visited[r][c - 2] = True
                prev[r][c - 1][0] = r
                prev[r][c - 1][1] = c
                prev[r][c - 2][0] = r
                prev[r][c - 2][1] = c - 1
            if r - 2 >= 0 and np.all(self.grid[r - 1][c] == [10, 206, 245]) and visited[r - 2][c] == False:
                rq.add(r - 2)
                cq.add(c)
                visited[r - 2][c] = True
                prev[r - 1][c][0] = r
                prev[r - 1][c][1] = c
                prev[r - 2][c][0] = r - 1
                prev[r - 2][c][1] = c
            if r + 2 < self.grid_size[0] and np.all(self.grid[r + 1][c] == [10, 206, 245]) and visited[r + 2][c] == False:
                rq.add(r + 2)
                cq.add(c)
                visited[r + 2][c] = True
                prev[r + 1][c][0] = r
                prev[r + 1][c][1] = c
                prev[r + 2][c][0] = r + 1
                prev[r + 2][c][1] = c

        #initialzing path(used for storing the path) and at (used as a pointer) which starts at the end coordinates
        path = []
        at = e

        #creating the path, editing the grid accordingly and displaying the grid on the canvas if there is a possible path, 
        #if there is no possible path, it pops up a message saying there is not path
        while np.all(at != [None,None]):
            path.append(at)
            at = prev[at[0]][at[1]]
        if reached_end:
            for coordinate in path:
                self.grid[coordinate[0]][coordinate[1]] = [0, 153, 0]
            self.display_array(self.grid)

        else:
            messagebox.showinfo("info", "path does not exist between the start and the end")
            

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
        
