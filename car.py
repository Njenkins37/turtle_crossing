from turtle import Turtle
import random

WIDTH = 1
HEIGHT = 2


def create_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    my_color = (r, g, b)
    return my_color


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.penup()
        self.car_list = []
        self.i = 1
        self.color(create_color())
        self.y = random.randint(-250, 250)
        self.goto(450, self.y)
        self.speed('fastest')

    def create_cars(self):
        car = Car()
        for i in range(0, 5):
            self.color(create_color())
            self.y = random.randint(-250, 250)
            self.goto(450, self.y)
            self.speed('fastest')
            self.car_list.append(car)

    def move(self):
        j = random.randint(0, 2)
        self.bk( j * self.i)

    def reset(self):
        self.y = random.randint(-250, 250)
        self.goto(450, self.y)

    def clear_car_list(self):
        self.car_list = []
