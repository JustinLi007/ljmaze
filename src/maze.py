from graphics import Cell, Point
from time import sleep

class Maze:
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            verbose=False,
            window=None
            ):
        self.__x = x
        self.__y = y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__verbose = verbose
        self.__window = window
        self.__cells = None

        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[Cell] * self.__num_cols] * self.__num_rows
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self.__draw_cell(i, j)
        if self.__verbose:
            self.__pretty_print()

    def __draw_cell(self, i, j):
        x = j * self.__cell_size_x + self.__x
        y = i * self.__cell_size_y + self.__y
        tl = Point(x, y)
        br = Point(tl.x + self.__cell_size_x, tl.y + self.__cell_size_y)
        self.__cells[i][j] = Cell(tl, br, self.__window)
        self.__cells[i][j].draw()
        if i == 0 and j == 0:
            print("PRE-COPY:", tl)
            print("PRE-COPY:", self.__cells[i][j])
            print("PRE-COPY:", self.__cells[i][j].get_top_left_corner())
            print("PRE-COPY:", self.__cells[i][j].get_bottom_right_corner())
        self.__animate()

    def __animate(self):
        if self.__window is None:
            return
        self.__window.redraw()
        sleep(0.01)

    def num_rows(self):
        if self.__cells is None:
            return 0
        return len(self.__cells)

    def num_cols(self):
        if self.__cells is None:
            return 0
        if self.__cells[0] is None:
            return 0
        return len(self.__cells[0])

    def get_grid(self):
        result = [[Cell] * self.__num_cols] * self.__num_rows
        for r in range(self.__num_rows):
            for c in range(self.__num_cols):
                cur_cell = self.__cells[r][c]
                print("COPY:", cur_cell.get_top_left_corner())
                print("COPY:", cur_cell.get_bottom_right_corner())
                result[r][c] = Cell(
                        cur_cell.get_top_left_corner(),
                        cur_cell.get_bottom_right_corner())
                result[r][c].draw()
                if r == 0 and c == 0:
                    print(cur_cell)
        return result

    def __pretty_print(self):
        for row in self.__cells:
            print(row)
