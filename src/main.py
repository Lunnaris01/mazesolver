from graphics import Window, Line,Point, Cell
from maze import Maze

def main():
    win = Window(800,600)
    cells = []
    maze = Maze(80,60,20,20,32,24,win)
    maze.create_cells()
    maze.draw_all_cells()
    maze._break_entrance_and_exit((0,0),(19,19),"N","S")
    print(maze.cells[0][0].walls)

    maze.break_walls_r(maze.num_rows//2,maze.num_cols//2)
    maze.reset_visited()
    maze.solve_r(0,0,19,19)

    win.wait_for_close()

    p1 = Point(50,50)
    p2 = Point(70,70)
    p3 = (p2-p1)//2
    print(p3)




if __name__  == '__main__':
    main()