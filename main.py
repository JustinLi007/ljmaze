from graphics import Window, Point, Line, Cell
import random

def main():
    window = Window(800, 600)
    cells = []
    for i in range(5):
        cells.append(
                Cell(Point(5+i*105, 10), Point(105+i*105, 100), window)
                )
        cells[i].has_left_wall = True if random.randint(0, 1) else False
        cells[i].has_right_wall = True if random.randint(0, 1) else False
        cells[i].has_top_wall =  True if random.randint(0, 1) else False
        cells[i].has_bottom_wall = True if random.randint(0, 1) else False

    for cell in cells:
        cell.draw()
    window.wait_for_close()
    print("Finish")

if __name__ == "__main__":
    main()
