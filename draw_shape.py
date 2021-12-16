import turtle

# The draw_shape main function is to collect all relevant data from asign2 and import it into Turtle drawing tool.
# turtle.speed controls speed of the drawing
turtle.speed(0)
scale = 10

def prepare_to_draw(position_x, position_y, colour):
    """
    prepare_to_draw() executes the main drawing operations which all other draw_(Shape) functions take from.
    draw_(shape) functions executes the main drawing procedures to draw the shape. The parameters are filled from
    users inputs from assign2 file
    """
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(position_x, position_y)
    turtle.pendown()
    turtle.begin_fill()

def draw_circle(radius, position_x, position_y, colour):
   prepare_to_draw(position_x, position_y, colour)
   turtle.circle(radius *scale)
   turtle.fillcolor(colour)
   turtle.end_fill()

def draw_square(length, position_x, position_y, colour):
    prepare_to_draw(position_x, position_y, colour)
    for i in range(4):
        turtle.fd(length *scale)
        turtle.lt(90)
    turtle.fillcolor(colour)
    turtle.end_fill()

def draw_triangle(base, position_x, position_y, colour):
    prepare_to_draw(position_x, position_y, colour)
    turtle.fd(base *scale)
    turtle.lt(120)
    turtle.fd(base *scale)
    turtle.left(120)
    turtle.fd(base *scale)
    turtle.fillcolor(colour)
    turtle.end_fill()
