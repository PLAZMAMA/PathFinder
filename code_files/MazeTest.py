from unittest import TestCase
from Maze import Maze

class MazeTest(TestCase):
    def setUp(self):
        self.maze = Maze((10,10))

    def test_create_grid(self):
        passed = True
        r = 0
        c = 1
        while passed and r < self.maze.grid_size[0]:
            if r % 2 == 0 and self.maze.grid[r][0] == [0,0,0] and passed:
                passed = False
            while passed and c < self.maze.grid_size[1]:
                if c % 2 == 0 and self.maze.grid[r][c] == [0, 0, 0]:
                    passed = False
                c += 1
            r += 1
            c = 1

        self.assertTrue(passed)

    def test_generate_maze(self):
        self.assertNotEqual(self.maze.generate_maze(), self.maze.generate_maze())
    
    def test_create_list(self):
        expected = [[None, None], [None, None], [None, None], [None, None]]
        self.assertEqual(expected, self.maze.create_list((4,2), None))
    
    def test_find_path(self):
        #creating the maze and the custom path set up
        self.maze = Maze((6, 6))
        self.maze.grid[1][0] = [10, 206, 245]
        self.maze.grid[1][1] = [10, 206, 245]
        self.maze.grid[1][2] = [10, 206, 245]
        self.maze.grid[3][0] = [10, 206, 245]
        self.maze.grid[3][1] = [10, 206, 245]
        self.maze.grid[3][2] = [10, 206, 245]
        self.maze.grid[5][0] = [10, 206, 245]
        self.maze.grid[6][1] = [10, 206, 245]
        self.maze.grid[6][3] = [10, 206, 245]
        self.maze.grid[6][5] = [10, 206, 245]
        self.maze.grid[6][7] = [10, 206, 245]
        self.maze.grid[6][9] = [10, 206, 245]
        self.maze.grid[7][6] = [10, 206, 245]
        self.maze.grid[7][10] = [10, 206, 245]
        self.maze.grid[8][5] = [10, 206, 245]
        self.maze.grid[9][4] = [10, 206, 245]
        self.maze.grid[9][10] = [10, 206, 245]
        self.maze.grid[10][5] = [10, 206, 245]
        self.maze.grid[10][7] = [10, 206, 245]
        self.maze.grid[10][9] = [10, 206, 245]

        #creating the expectd maze with the path
        expected = self.maze.grid
        expected[0][0] = [0, 153, 0]
        expected[1][0] = [0, 153, 0]
        expected[2][0] = [0, 153, 0]
        expected[3][0] = [0, 153, 0]
        expected[4][0] = [0, 153, 0]
        expected[5][0] = [0, 153, 0]
        expected[6][0] = [0, 153, 0]
        expected[6][1] = [0, 153, 0]
        expected[6][2] = [0, 153, 0]
        expected[6][3] = [0, 153, 0]
        expected[6][4] = [0, 153, 0]
        expected[6][5] = [0, 153, 0]
        expected[6][6] = [0, 153, 0]
        expected[6][7] = [0, 153, 0]
        expected[6][8] = [0, 153, 0]
        expected[6][9] = [0, 153, 0]
        expected[6][10] = [0, 153, 0]
        expected[7][10] = [0, 153, 0]
        expected[8][10] = [0, 153, 0]
        expected[9][10] = [0, 153, 0]
        expected[10][10] = [0, 153, 0]

        self.maze.find_path([0,0], [10, 10])
        self.assertEqual(expected, self.maze.grid)
