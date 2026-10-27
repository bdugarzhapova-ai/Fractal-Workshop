import turtle

turtle.left(90)
def draw_binary_tree(order, size, angle):
    if order == 0:
        return

    turtle.forward(size)

    position = turtle.pos()
    direction = turtle.heading()

    turtle.left(angle)
    draw_binary_tree(order - 1, size * 0.7, angle)

    turtle.penup()
    turtle.goto(position)
    turtle.setheading(direction)
    turtle.pendown()

    turtle.right(angle)
    draw_binary_tree(order - 1, size * 0.7, angle)

    turtle.penup()
    turtle.goto(position)
    turtle.setheading(direction)
    turtle.pendown()
    turtle.backward(size)

turtle.left(90)
def draw(size, order):
    if order == 0:
        turtle.left(180)
        return

    x = size / (order + 1)
    for i in range(order):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5 * x * (order - i - 1), order - i - 1)
        turtle.left(90)
        draw(0.5 * x * (order - i - 1), order - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)
    turtle.speed(0)
