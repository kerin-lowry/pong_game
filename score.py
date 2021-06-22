from turtle import Turtle

FONT_STYLE = ("Courier", 18, "normal")

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.refresh()
    
    
    def refresh(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Player A: {self.score_left}         Player B: {self.score_right}", align="center", font=FONT_STYLE)
    
    
    def update_score(self, player):
        if player == "left":
            self.score_left += 1
        if player == "right":
            self.score_right += 1
        self.refresh()