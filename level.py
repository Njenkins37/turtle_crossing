from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('white')
        self.penup()
        self.hideturtle()

    def add_level(self):
        self.level += 1

    def draw_finish_line(self):
        self.penup()
        self.goto(400, 300)
        for i in range(20):
            self.pendown()
            self.bk(20)
            self.penup()
            self.bk(20)
