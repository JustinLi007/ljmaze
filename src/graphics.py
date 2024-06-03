from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Maze")
        self.__canvas = Canvas(self.__root, bg="white", height=height,
                width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window closed")

    def close(self):
        self.__is_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
                self.__point1.x,
                self.__point1.y,
                self.__point2.x,
                self.__point2.y,
                fill=fill_color,
                width=2
                )

class Cell:
    def __init__(self, point1, point2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__point1 = point1
        self.__point2 = point2
        self.__window = window

    def draw_move(self, bottom_left_corner, target_cell, undo=False):
        fill_color = "gray" if undo else "red"
        self_center_point = Point(
                (self.__point2.x - self.__point1.x) / 2 + self.__point1.x,
                (self.__point2.y - self.__point1.y) / 2 + self.__point1.y
                )
        target_center_point = Point(
                (target_cell.__point2.x - target_cell.__point1.x) / 2 +
                target_cell.__point1.x,
                (target_cell.__point2.y - target_cell.__point1.y) / 2 +
                target_cell.__point1.y
                )
        path = Line(self_center_point, target_center_point)
        self.__window.draw_line(path, fill_color)

    def draw(self):
        if self.__window is None:
            return
        top_left_corner = self.__point1
        bottom_right_corner = self.__point2
        top_right_corner = Point(self.__point2.x, self.__point1.y)
        bottom_left_corner = Point(self.__point1.x, self.__point2.y)

        twall = Line(top_left_corner, top_right_corner)
        lwall = Line(top_left_corner, bottom_left_corner)
        bwall = Line(bottom_left_corner, bottom_right_corner)
        rwall = Line(top_right_corner, bottom_right_corner)

        if self.has_top_wall:
            self.__window.draw_line(twall, "black")
        else:
            self.__window.draw_line(twall, "white")

        if self.has_left_wall:
            self.__window.draw_line(lwall, "black")
        else:
            self.__window.draw_line(lwall, "white")

        if self.has_bottom_wall:
            self.__window.draw_line(bwall, "black")
        else:
            self.__window.draw_line(bwall, "white")

        if self.has_right_wall:
            self.__window.draw_line(rwall, "black")
        else:
            self.__window.draw_line(rwall, "white")

    def get_top_left_corner(self):
        tl = Point(self.__point1.x, self.__point1.y)
        return tl

    def get_bottom_right_corner(self):
        br = Point(self.__point2.x, self.__point2.y)
        return br
    
    def __repr__(self):
        top_left_corner = self.__point1
        bottom_right_corner = self.__point2
        top_right_corner = Point(self.__point2.x, self.__point1.y)
        bottom_left_corner = Point(self.__point1.x, self.__point2.y)
        return (
f"""
TL: {self.__point1} TR: {top_right_corner} BL: {bottom_left_corner} BR: {self.__point2}
"""
        )

