from turtle import *
from random import random, choice, randint

timmy = Turtle()
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    co = (r, g, b)
    return co


timmy.shape('circle')
timmy.pensize(15)
timmy.speed('fast')
directions = [0, 90, 180, 270]
for _ in range(100):
    timmy.color(random_color())
    timmy.setheading(directions[choice([0, 1, 2])]),
    timmy.forward(int(random() * 50))


exitonclick()
timmy.screen.mainloop()


