import math
import turtle

PALETTE = ["navy", "royalblue", "dodgerblue", "deepskyblue",
           "darkcyan", "teal", "seagreen", "black"]

NEST_1 = 4
NEST_2 = 1


def _set_color(level, use_color):
    turtle.pencolor(PALETTE[level % len(PALETTE)] if use_color else "black")


# Ледяной фрактал: вертикальная палка с перекладинами 
def _ruler(n, length, angle, level, use_color, nest=0, is_cross=False):
    if n == 0:
        _set_color(level, use_color)
        turtle.forward(length)
        return

    half = length / 2
    if nest > 0:
        cross_n, cross_nest = n, nest - 1
    else:
        cross_n, cross_nest = n - 1, 0

    _ruler(n - 1, half, angle, level + 1, use_color, nest)

    if not is_cross:
        turns = [angle] if angle == 90 else [angle, -angle]
        for t in turns:
            turtle.left(t)
            turtle.penup()
            turtle.backward(half / 2)
            turtle.pendown()
            _ruler(cross_n, half, angle, level + 1, use_color, cross_nest, True)
            turtle.penup()
            turtle.backward(half / 2)
            turtle.right(t)
            turtle.pendown()

    _ruler(n - 1, half, angle, level + 1, use_color, nest)


# Ледяной фрактал: главная горизонтальная ось, на которой растут кресты (или "V")
def _axis(n, length, angle, level, use_color, nest=0):
    if n == 0:
        _set_color(level, use_color)
        turtle.forward(length)
        return

    half = length / 2
    _axis(n - 1, half, angle, level + 1, use_color, nest)

    arm = length / 4
    headings = [angle] if angle == 90 else [angle, 180 - angle]
    for a in headings:
        turtle.left(a)
        _ruler(n - 1, arm, angle, level + 1, use_color, nest)
        turtle.penup()
        turtle.backward(arm)
        turtle.right(a)
        turtle.pendown()

    _axis(n - 1, half, angle, level + 1, use_color, nest)


# Ледяной фрактал №1: глубокая вложенность штрихов (NEST_1)
def ice_fractal_1(order, size, angle=90, use_color=True):
    _axis(order, size, angle, 0, use_color, NEST_1)


# Ледяной фрактал №2: маленькая вложенность штрихов (NEST_2)
def ice_fractal_2(order, size, angle=60, use_color=True):
    _axis(order, size, angle, 0, use_color, NEST_2)


# Кривая Леви: рекурсивное ядро
def _levy(n, size, angle, scale):
    if n == 0:
        turtle.forward(size)
        return
    turtle.left(angle)
    _levy(n - 1, size / scale, angle, scale)
    turtle.right(2 * angle)
    _levy(n - 1, size / scale, angle, scale)
    turtle.left(angle)


# Кривая Леви 
def levy(order, size, angle=45):
    scale = 2 * math.cos(math.radians(angle))
    _levy(order, size, angle, scale)
