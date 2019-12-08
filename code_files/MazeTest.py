from unittest import TestCase
from Maze import Maze

class MazeTest(TestCase):

    def test_create_grid(self):
        maze = Maze((10,10))
        passed = True
        r = 0
        c = 1
        while passed and r < maze.grid_size[0]:
            if r % 2 == 0 and maze.grid[r][0] == [0,0,0] and passed:
                passed = False
            while passed and c < maze.grid_size[1]:
                if c % 2 == 0 and maze.grid[r][c] == [0, 0, 0]:
                    passed = False
                c += 1
            r += 1
            c = 1

        self.assertTrue(passed)

    def test_generate_maze(self):
        maze = Maze((10,10))
        self.assertNotEqual(maze.generate_maze(), maze.generate_maze())