import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(700, 400)
screen.bgcolor("gray")
user_bet = screen.textinput(title="Make your bet?", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
ypos = [-100, -50, 0, 50, 100, 150]
israceon = False
all_turtles = []

for turtle_i in range(0, 6):
    newT = Turtle(shape="turtle")
    newT.color(color[turtle_i])
    newT.penup()
    newT.goto(x=-250, y=ypos[turtle_i])
    all_turtles.append(newT)
if user_bet:
    israceon = True


while israceon:

    for turtle in all_turtles:
        if turtle.xcor() > 250:
            israceon = False
            win = turtle.pencolor()
            if win == user_bet:
                turtle.write(f"THE WINNING COLOR IS {win}", align="center")
                print("YOU WON! THE WINNING COLOR IS = "+str(win))
            else:
                turtle.write(f"YOU LOSE!The {win} turtle has won!", align="center")
                print(f"You lose! {win} wins...")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()
