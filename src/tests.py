import unittest

from maze import Maze

class Test_Maze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10, False, None)
        self.assertEqual(m.num_cols(), num_cols)
        self.assertEqual(m.num_rows(), num_rows)

if __name__ == "__main__":
    unittest.main()
