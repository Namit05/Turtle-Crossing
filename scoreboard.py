FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("Black")
        self.penup()
        self.goto(-250, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level :{self.level}", align="center", font=("Courier", 14, "bold"))

    def update_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self) :
        self.goto(0,0)
        self.write(f"Game over!", align="center", font=("Courier", 25, "bold"))
        
