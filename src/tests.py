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

    def test_maze_cell_dims(self):
        num_cols = 5
        num_rows = 3
        x_margin = 50
        y_margin = 50
        x_len = 10
        y_len = 10
        m = Maze(x_margin, y_margin, num_rows,
                 num_cols, x_len, y_len, False, None)
        maze_grid = m.get_grid()
        for r in range(len(maze_grid)):
            for c in range(len(maze_grid[0])):
                cell = maze_grid[r][c]
                self.assertEqual(cell.get_bottom_right_corner().x
                                 - cell.get_top_left_corner().x, x_len)
                self.assertEqual(cell.get_bottom_right_corner().y
                                 - cell.get_top_left_corner().y, y_len)

    def test_maze_entrance_exit(self):
        num_cols = 5
        num_rows = 3
        x_margin = 50
        y_margin = 50
        x_len = 10
        y_len = 10
        m = Maze(x_margin, y_margin, num_rows, num_cols, x_len, y_len, False,
                 None)
        maze_grid = m.get_grid()
        first_cell = maze_grid[0][0]
        last_cell = maze_grid[num_rows-1][num_cols-1]
        self.assertFalse(first_cell.has_top_wall, "First cell has top wall")
        self.assertFalse(last_cell.has_bottom_wall,
                         "Last cell has bottomwall")


if __name__ == "__main__":
    unittest.main()
