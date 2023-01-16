from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,250)
        self.ht()
        self.color("white")

    def update(self, score):
        self.clear()
        self.write(f"Score: {score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over!", align=ALIGNMENT, font=FONT)