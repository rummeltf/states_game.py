from turtle import Turtle

# state name written at its location on the map
class StateName(Turtle):

    def __init__(self, name):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.write(f"{name}", font=("Times New Roman", 8, "normal"))

    def move(self, x, y):
        self.goto(x, y)