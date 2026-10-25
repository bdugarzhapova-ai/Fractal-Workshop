import turtle
import random
import math


# КРИВАЯ КОХА

def koch(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        koch(order - 1, size / 3)
        turtle.left(60)

        koch(order - 1, size / 3)
        turtle.right(120)

        koch(order - 1, size / 3)
        turtle.left(60)

        koch(order - 1, size / 3)


# СНЕЖИНКА КОХА

def koch_snowflake(order, size):
    turtle.fillcolor("lightblue")
    turtle.pencolor("blue")

    turtle.begin_fill()

    for i in range(3):
        koch(order, size)
        turtle.right(120)

    turtle.end_fill()


# КРИВАЯ МИНКОВСКОГО

def minkowski(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        minkowski(order - 1, size / 4)
        turtle.left(90)

        minkowski(order - 1, size / 4)
        turtle.right(90)

        minkowski(order - 1, size / 4)
        turtle.right(90)

        minkowski(order - 1, size / 4)

        minkowski(order - 1, size / 4)
        turtle.left(90)

        minkowski(order - 1, size / 4)
        turtle.left(90)

        minkowski(order - 1, size / 4)
        turtle.right(90)

        minkowski(order - 1, size / 4)


# КРИВАЯ КОХА СО СЛУЧАЙНЫМИ УГЛАМИ

def koch_random(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        angle = random.uniform(50, 70)

        small_size = size / (
            2 + 2 * math.cos(math.radians(angle))
        )

        koch_random(order - 1, small_size)
        turtle.left(angle)

        koch_random(order - 1, small_size)
        turtle.right(2 * angle)

        koch_random(order - 1, small_size)
        turtle.left(angle)

        koch_random(order - 1, small_size)

