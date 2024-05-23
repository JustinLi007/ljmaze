from graphics import Cell, Point

class Maze:
    def __init__(
            self,
            x,
            y,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window
            ):
        self.__x = x
        self.__y = y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window

        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[Cell] * self.__num_cols] * self.__num_rows
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self.__draw_cell(i, j)
        self.__pretty_print()

    def __draw_cell(self, i, j):
        x = j * self.__cell_size_x + self.__x
        y = i * self.__cell_size_y + self.__y
        tl = Point(x, y)
        br = Point(tl.x + self.__cell_size_x, tl.y + self.__cell_size_y)
        self.__cells[i][j] = Cell(tl, br, self.__window)
        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self):
        #self.__window.__root.after(50, func=self.__window.redraw)
        pass

    def __pretty_print(self):
        for row in self.__cells:
            print(row)
