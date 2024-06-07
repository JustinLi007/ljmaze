from graphics import Cell, Point
from time import sleep
import random

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
            window=None,
            seed=None
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
        self.__seed = seed

        if self.__seed is not None:
            random.seed(self.__seed);

        self.__create_cells()

    def __create_cells(self):
        self.__cells = [
                [None for _ in range(self.__num_cols)] for _ in
                range(self.__num_rows)
                ]
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self.__draw_cell(i, j)
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        if self.__verbose:
            self.__pretty_print()

    def __draw_cell(self, i, j):
        x = j * self.__cell_size_x + self.__x
        y = i * self.__cell_size_y + self.__y
        tl = Point(x, y)
        br = Point(tl.x + self.__cell_size_x, tl.y + self.__cell_size_y)
        self.__cells[i][j] = Cell(tl, br, self.__window)
        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self, sleep_duration=0.002):
        if self.__window is None:
            return
        self.__window.redraw()
        sleep(sleep_duration)

    def __break_entrance_and_exit(self): 
        if self.__cells is None:
            return
        self.__cells[0][0].has_top_wall = False
        self.__cells[0][0].draw()
        self.__cells[self.__num_rows-1][self.__num_cols-1].has_bottom_wall = False
        self.__cells[self.__num_rows-1][self.__num_cols-1].draw()
        self.__animate()

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            directions = []
            if i - 1 >= 0 and not self.__cells[i-1][j].visited:
                directions.append((i-1, j))
            if i + 1 <= self.__num_rows - 1 and not self.__cells[i+1][j].visited:
                directions.append((i+1, j))
            if j - 1 >= 0 and not self.__cells[i][j-1].visited:
                directions.append((i, j-1))
            if j + 1 <= self.__num_cols - 1 and not self.__cells[i][j+1].visited:
                directions.append((i, j+1))

            if len(directions) == 0:
                self.__cells[i][j].draw()
                self.__animate()
                return

            rand_dir = random.randint(0, len(directions)-1)
            next_i, next_j = directions[rand_dir]
             
            i_diff = i - next_i
            j_diff = j - next_j
            if i_diff == 0 and j_diff < 0:
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_i][next_j].has_left_wall = False
            elif i_diff == 0 and j_diff > 0:
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_i][next_j].has_right_wall = False
            elif j_diff == 0 and i_diff < 0:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_i][next_j].has_top_wall = False
            elif j_diff == 0 and i_diff > 0:
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False

            self.__break_walls_r(next_i, next_j)

    def solve(self, type=0):
        start = (0,0)
        end = (self.__num_rows-1, self.__num_cols-1)
        result = None
        if type == 0:
            result = self.__solve_r_bfs(start, end)
        else:
            result = self.__solve_r_dfs(start, end)
        return result

    def __solve_r_bfs(self, start, end):
        queue = []
        queue.append((start, (start,)))
        prev = None
        while len(queue) > 0:
            element = queue.pop(0)
            x, y = element[0]
            cell = self.__cells[x][y]
            cell.visited = True

            if not cell.has_top_wall and x-1 >= 0 and not self.__cells[x-1][y].visited:
                step = (x-1, y)
                queue.append((step, element[1] + (step,)))
            if not cell.has_right_wall and y+1 <= self.__num_cols-1 and not self.__cells[x][y+1].visited:
                step = (x, y+1)
                queue.append((step, element[1] + (step,)))
            if not cell.has_bottom_wall and x+1 <= self.__num_rows-1 and not self.__cells[x+1][y].visited:
                step = (x+1, y)
                queue.append((step, element[1] + (step,)))
            if not cell.has_left_wall and y-1 >= 0 and not self.__cells[x][y-1].visited:
                step = (x, y-1)
                queue.append((step, element[1] + (step,)))
       
            sleep_duration = 0.005
            if prev is not None:
                path = prev[1]
                path_len = len(path)
                for i in range(1, path_len):
                    from_cell = self.__cells[path[i-1][0]][path[i-1][1]]
                    to_cell = self.__cells[path[i][0]][path[i][1]]
                    from_cell.draw_move(to_cell, True)
                self.__animate(sleep_duration)
            
            path = element[1]
            path_len = len(path)
            for i in range(1, path_len):
                from_cell = self.__cells[path[i-1][0]][path[i-1][1]]
                to_cell = self.__cells[path[i][0]][path[i][1]]
                from_cell.draw_move(to_cell)
                if i == path_len - 2:
                    break
            self.__animate(sleep_duration * 1.5)
 
            from_cell = self.__cells[path[path_len-2][0]][path[path_len-2][1]]
            to_cell = self.__cells[path[path_len-1][0]][path[path_len-1][1]]
            from_cell.draw_move(to_cell)
            self.__animate(sleep_duration * 1.5)

            prev = element
            if (x,y) == end:
                return (True, queue)
        return (False, None)

    def __solve_r_dfs(self, start, end):
        stack = []
        stack.append((start, (start,)))
        prev = None
        while len(stack) > 0:
            element = stack.pop()
            x, y = element[0]
            cell = self.__cells[x][y]
            cell.visited = True

            if not cell.has_top_wall and x-1 >= 0 and not self.__cells[x-1][y].visited:
                step = (x-1, y)
                stack.append((step, element[1] + (step,)))
            if not cell.has_right_wall and y+1 <= self.__num_cols-1 and not self.__cells[x][y+1].visited:
                step = (x, y+1)
                stack.append((step, element[1] + (step,)))
            if not cell.has_bottom_wall and x+1 <= self.__num_rows-1 and not self.__cells[x+1][y].visited:
                step = (x+1, y)
                stack.append((step, element[1] + (step,)))
            if not cell.has_left_wall and y-1 >= 0 and not self.__cells[x][y-1].visited:
                step = (x, y-1)
                stack.append((step, element[1] + (step,)))
       
            sleep_duration = 0.0025
            if prev is not None:
                path = prev[1]
                path_len = len(path)
                for i in range(1, path_len):
                    from_cell = self.__cells[path[i-1][0]][path[i-1][1]]
                    to_cell = self.__cells[path[i][0]][path[i][1]]
                    from_cell.draw_move(to_cell, True)
                self.__animate(sleep_duration)
            
            path = element[1]
            path_len = len(path)
            for i in range(1, path_len):
                from_cell = self.__cells[path[i-1][0]][path[i-1][1]]
                to_cell = self.__cells[path[i][0]][path[i][1]]
                from_cell.draw_move(to_cell)
                if i == path_len - 2:
                    break
            self.__animate(sleep_duration * 1.5)
 
            from_cell = self.__cells[path[path_len-2][0]][path[path_len-2][1]]
            to_cell = self.__cells[path[path_len-1][0]][path[path_len-1][1]]
            from_cell.draw_move(to_cell)
            self.__animate(sleep_duration * 1.5)

            prev = element
            if (x,y) == end:
                return (True, stack)
        return (False, None)

    def __reset_cells_visited(self):
        for r in range(self.__num_rows):
            for c in range(self.__num_cols):
                self.__cells[r][c].visited = False

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
        result = [
                [None for _ in range(self.__num_cols)] for _ in
                range(self.__num_rows)
                ]
        for r in range(self.__num_rows):
            for c in range(self.__num_cols):
                cur_cell = self.__cells[r][c]
                result[r][c] = Cell(
                        cur_cell.get_top_left_corner(),
                        cur_cell.get_bottom_right_corner()
                        )
                result[r][c].has_top_wall = cur_cell.has_top_wall
                result[r][c].has_bottom_wall = cur_cell.has_bottom_wall
                result[r][c].has_left_wall = cur_cell.has_left_wall
                result[r][c].has_right_wall = cur_cell.has_right_wall
        return result

    def __pretty_print(self):
        print(self.__cells)
        #for row in self.__cells:
        #    print(row)
