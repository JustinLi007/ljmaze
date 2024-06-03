from graphics import Window, Point, Line, Cell
from maze import Maze
import random

def main():
    WIN_WIDTH = 800
    WIN_HEIGHT = 600
    ROWS = 12
    COLS = 16
    X_OFFSET = 50
    Y_OFFSET = 50
    CELL_WIDTH = (WIN_WIDTH - 2 * X_OFFSET) / COLS
    CELL_HEIGHT = (WIN_HEIGHT - 2 * Y_OFFSET) / ROWS
    
    window = Window(WIN_WIDTH, WIN_HEIGHT)
    maze = Maze(
            X_OFFSET,
            Y_OFFSET,
            ROWS,
            COLS,
            CELL_WIDTH,
            CELL_HEIGHT,
            False,
            window,
            None)
    
    maze_grid = maze.get_grid()

    window.wait_for_close()
    print("Finish")
    return 0

if __name__ == "__main__":
    main()
