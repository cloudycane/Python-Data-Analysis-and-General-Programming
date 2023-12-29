import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.pensize(6)
tim.speed("fastest")


screen = Screen()
screen.bgcolor("sea green")
tim.color("white")
tim.write("This is a blackboard, use your keyboard keys to draw. \n ASWD = movement, U= pen up, I= pen down", font=("Verdana", 10, "normal"), align="center")

def move_f():
    tim.forward(10)

def move_b():
    tim.forward(-10)

def move_c():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def move_cc():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_d():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def pen_up():
    tim.penup()

def pen_down():
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_f)
screen.onkey(key="s", fun=move_b)
screen.onkey(key="d", fun=move_c)
screen.onkey(key="a", fun=move_cc)
screen.onkey(key="c", fun=clear_d)
screen.onkey(key="u", fun=pen_up)
screen.onkey(key="i", fun=pen_down)
screen.exitonclick()