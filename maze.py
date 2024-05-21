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
        # TODO: create cells.
        
        self.__animate()

    def __animate(self):
        self.__window.after(50, self.__window.redraw)

    def __pretty_print(self):
        for row in self.__cells:
            print(row)
