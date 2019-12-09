import random
from Stack import Stack
import numpy as np
from Queue import Queue

class Maze():
    def __init__(self, size):
        self.grid_size = size
        self.grid_size[0] = self.grid_size[0] * 2 - 1 
        self.grid_size[1] = self.grid_size[1] * 2 - 1

        #generates the grid with black walls in between each blue cell
        #creates the output array with the corrected sizes
        self.grid = np.zeros((self.grid_size[0], self.grid_size[1], 3), dtype = np.int32)

        #loops and creates the walls and cells in the grid array(making the grid)
        for r in range(self.grid_size[0]):
            if r % 2 == 0:
                for c in range(self.grid_size[1]):
                    if c % 2 == 0:
                        self.grid[r][c] = [10, 206, 245]
                    else:
                        self.grid[r][c] = [0, 0, 0]
            else:
                for c in range(self.grid_size[1]):
                    self.grid[r][c] = [0, 0, 0]
    
    def get_neighbors(self, r, c, visited):
        """return the unvisited neightbors given the row, column of the neighbors and the current visited array"""
        neighbors = []
        if c + 2 < self.grid_size[1] and visited[r][c + 2] == False:
            neighbors.append("right")
        if c - 2 > 0 and visited[r][c - 2] == False:
            neighbors.append("left")
        if r - 2 > 0 and visited[r - 2][c] == False:
            neighbors.append("up")
        if r + 2 < self.grid_size[0] and visited[r + 2][c] == False:
            neighbors.append("down")
        
        return(neighbors)
        
    
    def generate_maze(self):
        """generates a maze into the grid"""
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
            neighbors = self.get_neighbors(r, c, visited)

            # choosing a neighbor at random if there are any neighbors, displaying it, adding the coordinates to the stack, making the current node's locaions right
            if len(neighbors) > 0:
                choice = random.choice(neighbors)
                if choice == "right":
                    self.grid[r][c + 1] = [10, 206, 245]
                    c += 2
                    visited[r][c] = True
                    c_stack.add(c)
                    r_stack.add(r)
                elif choice == "left":
                    self.grid[r][c - 1] = [10, 206, 245]
                    c -= 2
                    visited[r][c] = True
                    c_stack.add(c)
                    r_stack.add(r)
                elif choice == "up":
                    self.grid[r - 1][c] = [10, 206, 245]
                    r -= 2
                    visited[r][c] = True
                    c_stack.add(c)
                    r_stack.add(r)
                else:
                    self.grid[r + 1][c] = [10, 206, 245]
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
    
    def create_list(self, size, val):
        """creates a certain size list"""
        l = []
        if len(size) == 1:
            for _ in range(size[0]):
                l.append(val)
            return(l)

        else:
            for _ in range(size[0]):
                l.append(self.create_list(size[1:], val))
            return(l)

    def find_path(self, s, e):
        """finds the path from s to e and updates the grid with the found path and returns if it was able to reach the end"""
        #initializing the queues
        rq = Queue()
        cq = Queue()

        #initially marking reached end as false (used to know if the end is reachable)
        reached_end = False

        #initializing the visited array to keep track of visited nodes and a prev array to keep track of the path
        visited = np.zeros((self.grid_size[0], self.grid_size[1]), dtype = np.bool)
        prev = self.create_list((self.grid_size[0], self.grid_size[1], 2), None)
        
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
                prev[r][c + 1] = [r, c]
                prev[r][c + 2] = [r, c + 1]
            if c - 2 >= 0 and np.all(self.grid[r][c - 1] == [10, 206, 245]) and visited[r][c - 2] == False:
                rq.add(r)
                cq.add(c - 2)
                visited[r][c - 2] = True
                prev[r][c - 1] = [r, c]
                prev[r][c - 2] = [r, c - 1]
            if r - 2 >= 0 and np.all(self.grid[r - 1][c] == [10, 206, 245]) and visited[r - 2][c] == False:
                rq.add(r - 2)
                cq.add(c)
                visited[r - 2][c] = True
                prev[r - 1][c] = [r, c]
                prev[r - 2][c] = [r - 1, c]
            if r + 2 < self.grid_size[0] and np.all(self.grid[r + 1][c] == [10, 206, 245]) and visited[r + 2][c] == False:
                rq.add(r + 2)
                cq.add(c)
                visited[r + 2][c] = True
                prev[r + 1][c] = [r, c]
                prev[r + 2][c] = [r + 1, c]
        
        self.create_path(prev, e, reached_end)
        return(reached_end)

    def create_path(self, prev, e, reached_end):
        """creates the path from the given prev and end point"""

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
