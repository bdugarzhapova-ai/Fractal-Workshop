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
def draw_branch(order, size):
    if order == 0:
        return

    position = turtle.pos()
    angle = turtle.heading()

    turtle.forward(size)

    branch_position = turtle.pos()
    branch_angle = turtle.heading()

    turtle.left(45)
    draw_branch(order - 1, size / 2)

    turtle.penup()
    turtle.goto(branch_position)
    turtle.setheading(branch_angle)
    turtle.pendown()

    turtle.right(45)
    draw_branch(order - 1, size / 2)
  
    turtle.penup()
    turtle.goto(branch_position)
    turtle.setheading(branch_angle)
    turtle.pendown()
  
    draw_branch(order - 1, size * 0.7)
  
    turtle.penup()
    turtle.goto(position)
    turtle.setheading(angle)
    turtle.pendown()

turtle.speed(0)
draw_binary_tree(5,100,45)
