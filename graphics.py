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

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
                self.__point1.x,
                self.__point1.y,
                self.__point2.x,
                self.__point2.y,
                fill=fill_color,
                width=2
                )

class Cell:
    def __init__(self, point1, point2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__point1 = point1
        self.__point2 = point2
        self.__window = window

    def draw(self):
        top_left_corner = self.__point1
        bottom_right_corner = self.__point2
        top_right_corner = Point(
                self.__point1.x + (self.__point2.x - self.__point1.x),
                self.__point2.y - (self.__point2.y - self.__point1.y)
                )
        bottom_left_corner = Point(
                self.__point2.x - (self.__point2.x - self.__point1.x),
                self.__point1.y + (self.__point2.y - self.__point1.y)
                )
        print(
                (f"TL: {(top_left_corner.x, top_left_corner.y)}"),
                (f"TR: {(top_right_corner.x, top_right_corner.y)}"),
                (f"BL: {(bottom_left_corner.x, bottom_left_corner.y)}"),
                (f"BR: {(bottom_right_corner.x, bottom_right_corner.y)}"),
                )
        if self.has_top_wall:
            wall = Line(top_left_corner, top_right_corner)
            self.__window.draw_line(wall, "black")
        if self.has_left_wall:
            wall = Line(top_left_corner, bottom_left_corner)
            self.__window.draw_line(wall, "black")
        if self.has_bottom_wall:
            wall = Line(bottom_left_corner, bottom_right_corner)
            self.__window.draw_line(wall, "black")
        if self.has_right_wall:
            wall = Line(top_right_corner, bottom_right_corner)
            self.__window.draw_line(wall, "black")

