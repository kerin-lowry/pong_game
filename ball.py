from turtle import Turtle

DX = 0.1
DY = 0.1

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.dx = DX
        self.dy = DY
    
    
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
    
    
    def bounce_y(self):
        self.dy *= -1
    
    
    def bounce_x(self):
        self.dx *= -1
    
    
    def recenter(self):
        self.goto(0,0)
        self.bounce_x()
        self.dx = DX
        self.dy = DY
    
    
    def speed_up(self):
        self.dx *= 1.2
        self.dy *= 1.2
    