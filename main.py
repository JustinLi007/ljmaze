from graphics import Window, Point, Line, Cell
from maze import Maze
import random

def main():
    WIN_WIDTH = 800
    WIN_HEIGHT = 600
    ROWS = 5
    COLS = 5
    CELL_WIDTH = 100
    CELL_HEIGHT = 100
    X_OFFSET = 50
    Y_OFFSET = 50
    
    window = Window(WIN_WIDTH, WIN_HEIGHT)
    maze = Maze(
            X_OFFSET,
            Y_OFFSET,
            ROWS,
            COLS,
            CELL_WIDTH,
            CELL_HEIGHT,
            window)

    window.wait_for_close()
    print("Finish")

if __name__ == "__main__":
    main()
