from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.circle(100)
tim.speed("fastest")

def draw_spiro(gap):
    for _ in range(int(360 / gap)):

        current_h = tim.heading()
        tim.setheading(current_h + 10)
        tim.circle(100)
draw_spiro(10)

screen.exitonclick()