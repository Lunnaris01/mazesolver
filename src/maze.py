import time
from graphics import Cell, Line, Point, Window
import random

class Maze():
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=1337):
        self.x=x1
        self.y=y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        random.seed(seed)

    def create_cells(self):
        self.cells = [[Cell("NESW",Point(self.x+self.cell_size_x*rowindex,self.y+self.cell_size_y*colindex),Point(self.x+self.cell_size_x*(rowindex+1),self.y+self.cell_size_y*(colindex+1))) for rowindex in range(self.num_rows)] for colindex in range(self.num_cols)]

    def draw_all_cells(self):
        for line in self.cells:
            for cell in line:
                self.draw_cell(cell)

    def draw_cell(self,cell):
        self.win.draw_cell(cell)

    def animate(self):
        self.win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self,entrance,exit,entrancewall,exitwall):
        x,y = entrance
        cell = self.cells[x][y]
        self.remove_wall(cell,entrancewall)
        x,y = exit
        cell = self.cells[x][y]
        self.remove_wall(cell,exitwall)

    def remove_walls(self,cell,walls):
        for wall in walls:
            self.remove_wall(cell,wall)
    
    def remove_wall(self,cell,wall):
        print(cell.walls,wall)
        cell.walls = cell.walls.replace(wall,"")
        self.draw_cell(cell)
        print(cell.walls)
    
    def break_walls_r(self,i,j):
        self.cells[i][j].visited = True
        to_visit = []
        adjacent_cells = self.get_adj_cells(i,j)
        random.shuffle(adjacent_cells)
        for cellindizes in adjacent_cells:
            if not self.cells[cellindizes[0]][cellindizes[1]].visited:
                to_visit.append(cellindizes)
        for nextnode in to_visit:
            if not self.cells[nextnode[0]][nextnode[1]].visited:
                self.remove_wall(self.cells[i][j],nextnode[2])
                self.remove_wall(self.cells[nextnode[0]][nextnode[1]],nextnode[3])
                self.break_walls_r(nextnode[0],nextnode[1])

    def get_adj_cells(self, i, j):
        adj_list = []
        if i - 1 >= 0:  # Top boundary check
            adj_list.append([i - 1, j, "N", "S"])  # Moving up knocks down "N"
        if i + 1 < self.num_rows:  # Bottom boundary check
            adj_list.append([i + 1, j, "S", "N"])  # Moving down knocks down "S"
        if j - 1 >= 0:  # Left boundary check
            adj_list.append([i, j - 1, "W", "E"])  # Moving left knocks down "W"
        if j + 1 < self.num_cols:  # Right boundary check
            adj_list.append([i, j + 1, "E", "W"])  # Moving right knocks down "E"
        return adj_list
    
    def reset_visited(self):
        for line in self.cells:
            for cell in line:
                cell.visited = False


    def solve_r(self,x,y,endx,endy):
        self.animate()
        print(x,y,endx,endy)
        current_cell = self.cells[x][y]
        current_cell.visited = True
        if x==endx and y == endy:
            return True
        to_visit = []
        adj_cells = self.get_adj_cells(x,y)
        random.shuffle(adj_cells)
        for cellindizes in adj_cells:
            if not self.cells[cellindizes[0]][cellindizes[1]].visited and cellindizes[2] not in current_cell.walls:
                to_visit.append(cellindizes)
        for nextnode in to_visit:
            if not self.cells[nextnode[0]][nextnode[1]].visited:
                current_cell.draw_move(self.win.canvas,self.cells[nextnode[0]][nextnode[1]],"red")
                if self.solve_r(nextnode[0],nextnode[1],endx,endy):
                    return True
                else:
                    current_cell.draw_move(self.win.canvas,self.cells[nextnode[0]][nextnode[1]],"gray")
                    self.animate()


