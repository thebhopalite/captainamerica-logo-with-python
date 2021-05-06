import turtle
import math

captain = turtle.Turtle()

def star(r, color):
    start(0, 0)
    captain.pencolor(color)
    captain.setheading(162)
    captain.forward(r)
    captain.setheading(0)
    captain.fillcolor(color)
    captain.begin_fill()
    for i in range(5):
        captain.forward(math.cos(math.radians(18)) * 2 * r) 
        captain.right(144)
    captain.end_fill()
    captain.hideturtle()

def start(x, y):
    captain.penup()
    captain.goto(x, y)
    captain.pendown()
    captain.setheading(0)
    captain.pensize(2)
    captain.speed(10)    
    
def mid(r, color):
    x_point = 0
    y_pont = -r
    start(x_point, y_pont)
    captain.pencolor(color)
    captain.fillcolor(color)
    captain.begin_fill()
    captain.circle(r)
    captain.end_fill()


if __name__ == '__main__':
    mid(288, 'crimson')
    mid(234, 'snow')
    mid(174, 'crimson')
    mid(114, 'blue')
    star(114, 'snow')
    turtle.done()