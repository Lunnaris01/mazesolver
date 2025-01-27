from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title = "Mazesolver"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root,bg = 'white',height=self.height,width=self.width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def draw_line(self,line,fill_color="black"):
        line.draw(self.canvas,fill_color)

    def draw_cell(self,cell,fill_color="black"):
        cell.draw(self.canvas,fill_color)

    def draw_cellmove(self,cell,other_cell,fill_color="red",undo=False):
        cell.draw_move(self.canvas,other_cell,fill_color,undo)

    def wait_for_close(self):
        self.running = True
        while(self.running):
            self.redraw()

    def close(self):
        self.running = False

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Point(self.x-other.x,self.y-other.y)      

    def __floordiv__(self,divisor:int):
        return Point(self.x//divisor,self.y//divisor)
    def __repr__(self):
        return f'Point(x:{self.x},y:{self.y})'

class Line():
    def __init__(self,start:Point,end:Point):
        self.start = start
        self.end = end

    def draw(self,canvas,fill_color):
        canvas.create_line(self.start.x,self.start.y,self.end.x,self.end.y,fill = fill_color, width=2)


        
class Cell():
    def __init__(self,walls,topleft:Point,bottomright:Point):
        self.walls=walls
        self.topleft = topleft
        self.bottomright = bottomright
        self.topright = Point(bottomright.x,topleft.y)
        self.bottomleft = Point(topleft.x,bottomright.y)
        self.centerpoint = self.topleft + (self.bottomright-self.topleft)//2
        self.visited = False

    def draw(self,canvas:Canvas,fill_color):
        if 'N' in self.walls:
            canvas.create_line(self.topleft.x,self.topleft.y,self.topright.x,self.topright.y,fill=fill_color, width=2)
        else:
            canvas.create_line(self.topleft.x,self.topleft.y,self.topright.x,self.topright.y,fill="white", width=2)
        if 'E' in self.walls:
            canvas.create_line(self.topright.x,self.topright.y,self.bottomright.x,self.bottomright.y,fill=fill_color, width=2)
        else:
            canvas.create_line(self.topright.x,self.topright.y,self.bottomright.x,self.bottomright.y,fill="white", width=2)
        if 'S' in self.walls:
            canvas.create_line(self.bottomleft.x,self.bottomleft.y,self.bottomright.x,self.bottomright.y,fill=fill_color, width=2)
        else:
            canvas.create_line(self.bottomleft.x,self.bottomleft.y,self.bottomright.x,self.bottomright.y,fill="white", width=2)
        if 'W' in self.walls:
            canvas.create_line(self.topleft.x,self.topleft.y,self.bottomleft.x,self.bottomleft.y,fill=fill_color, width=2)
        else:
            canvas.create_line(self.topleft.x,self.topleft.y,self.bottomleft.x,self.bottomleft.y,fill="white", width=2)
        

    def draw_move(self,canvas:Canvas,target_cell,fill_color,undo=False):
        canvas.create_line(self.centerpoint.x,self.centerpoint.y,target_cell.centerpoint.x,target_cell.centerpoint.y,fill=fill_color,width=2)
