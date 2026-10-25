import math
import turtle

# Глубина вложенности перекладин для снежинок
NEST_1 = 4  # Для Ледяного фрактала №1 (густой, прямые кресты)
NEST_2 = 1  # Для Ледяного фрактала №2 (простой, с "V" и снежинками)


# Ледяной фрактал: вертикальная палка с перекладинами 
def _ruler(n, length, angle, nest=0, is_cross=False):
    if n == 0:
        turtle.forward(length)
        return

    half = length / 2
    if nest > 0:
        cross_n, cross_nest = n, nest - 1
    else:
        cross_n, cross_nest = n - 1, 0

    _ruler(n - 1, half, angle, nest)

    if not is_cross:
        turns = [angle] if angle == 90 else [angle, -angle]
        for t in turns:
            turtle.left(t)
            turtle.penup()
            turtle.backward(half / 2)
            turtle.pendown()
            _ruler(cross_n, half, angle, cross_nest, True)
            turtle.penup()
            turtle.backward(half / 2)
            turtle.right(t)
            turtle.pendown()

    _ruler(n - 1, half, angle, nest)


# Ледяной фрактал: главная горизонтальная ось, на которой растут кресты (или "V")
def _axis(n, length, angle, nest=0):
    if n == 0:
        turtle.forward(length)
        return

    half = length / 2
    _axis(n - 1, half, angle, nest)

    arm = length / 4
    headings = [angle] if angle == 90 else [angle, 180 - angle]
    for a in headings:
        turtle.left(a)
        _ruler(n - 1, arm, angle, nest)
        turtle.penup()
        turtle.backward(arm)
        turtle.right(a)
        turtle.pendown()

    _axis(n - 1, half, angle, nest)


# Ледяной фрактал №1: глубокая вложенность перекладин (NEST_1)
def ice_fractal_1(order, size, angle=90):
    _axis(order, size, angle, NEST_1)


# Ледяной фрактал №2: маленькая вложенность перекладин (NEST_2)
def ice_fractal_2(order, size, angle=60):
    _axis(order, size, angle, NEST_2)


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
