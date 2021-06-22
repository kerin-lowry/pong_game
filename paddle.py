from turtle import Turtle

MOVE_SIZE = 20

class Paddle(Turtle):
    
    def __init__(self, xpos):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xpos, 0)
    
    
    def go_up(self):
        y = self.ycor() + MOVE_SIZE
        self.sety(y)
    
    
    def go_down(self):
        y = self.ycor() - MOVE_SIZE
        self.sety(y)
    