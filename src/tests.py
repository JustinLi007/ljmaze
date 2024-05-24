import unittest

from maze import Maze
from graphics import Window

class Test_Maze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10, False, None)
        self.assertEqual(m.num_cols(), num_cols)
        self.assertEqual(m.num_rows(), num_rows)
        
    def test_maze_margin(self):
        num_cols = 5
        num_rows = 3
        x_margin = 50
        y_margin = 50
        m = Maze(x_margin, y_margin, num_rows, num_cols, 10, 10, False, None)
        maze_grid = m.get_grid()
        tl = maze_grid[0][0].get_top_left_corner()
        self.assertEqual(tl.x, x_margin)
        self.assertEqual(tl.y, y_margin)

if __name__ == "__main__":
    unittest.main()
