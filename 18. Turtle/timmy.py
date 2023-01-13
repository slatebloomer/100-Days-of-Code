import turtle as t
import random


def right_forward():
    timmy.rt(90)
    timmy.forward(100)


timmy = t.Turtle()
t.colormode(255)
timmy.shape("arrow")
timmy.color("darkgreen")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


def polygon(angle_count):
    angle = 360 / angle_count
    for i in range(angle_count):
        timmy.forward(100)
        timmy.right(angle)


def turn():
    choice = random.randint(1,2)
    if choice == 1:
        return timmy.right(90)
    else:
        return timmy.left(90)


def random_walk():
    while True:
        timmy.forward(random.randint(20, 100))
        turn()
        timmy.color(random_colour())

timmy.speed("fastest")
for _ in range(100):
    timmy.circle(100)
    timmy.rt(3.65)
    timmy.color(random_colour())

screen = t.Screen()
screen.exitonclick()
