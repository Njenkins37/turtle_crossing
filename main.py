from turtle import Turtle, Screen
from car import Car
from level import Level


def move_up():
    t.fd(40)


def move_down():
    t.bk(40)


def move_right():
    new_x = t.xcor() + 40
    t.goto(new_x, t.ycor())


def move_left():
    new_x = t.xcor() - 40
    t.goto(new_x, t.ycor())

if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor('black')
    screen.setup(width=800, height=800)
    screen.colormode(255)
    screen.listen()
    screen.tracer(0)

    level = Level()




    screen.onkey(move_up, 'Up')
    screen.onkey(move_down, 'Down')
    screen.onkey(move_right, 'Right')
    screen.onkey(move_left, 'Left')

    game_is_on = True

    collision_list = []
    car_list = []

    for i in range(5):
        car = Car()
        car_list.append(car)

    t = Turtle('turtle')
    t.color('green')
    t.penup()
    t.goto(0, -350)
    t.speed('slowest')
    t.seth(90)

    level.goto(-300, 300)
    level.clear()

    while game_is_on:

        level.write(arg=f'Level: {level.level}', font=('Courier', 24, 'normal'), move=False)
        level.draw_finish_line()
        screen.update()

        for car in car_list:
            car.move()
            if car.xcor() < -400:
                car.reset()
            if t.distance(car) < 25:
                collision_list.append(True)
        if t.ycor() > 300:
            print('entered')
            level.add_level()
            level.clear()
            t.goto(0, -350)
            for car in car_list:
                car.i += 0.5
            for i in range(5):
                car = Car()
                car_list.append(car)
        if any(collision_list):
            game_is_on = False

    screen.exitonclick()
