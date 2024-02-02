"""
This program will randomly draw 100 squares on the screen when it is run.
the squares will change both color and position for each one.
The colors cycle between blue,red, green, and yellow.
The side of each square is 20
author: Sam Jackson email:sjackso2@malcalester.edu
"""
import turtle
import random
window = turtle.Screen()
square = turtle.Turtle()
window.bgcolor("light grey")
square.speed(0)
sqColors = ["blue", "red", "green", "yellow"]
for i in range(100):
    square.penup()
    square.color(random.choice(sqColors))
    square.goto(random.randint(-250,250), random.randint(-250,250))
    square.pendown()
    square.begin_fill()
    for m in range(4):
        square.forward(20)
        square.left(90)
    square.end_fill()
window.exitonclick()