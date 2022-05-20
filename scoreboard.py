from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=FONT)
