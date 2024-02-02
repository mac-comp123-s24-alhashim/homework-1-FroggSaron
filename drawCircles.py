"""
Draws six circles, centered on the origin, each a different color.
Assumption: the number of colors in the turtle colors list is at least
as long as the number of rings.
"""


import turtle
import math

scr = turtle.Screen()
# changed mispelled Turtel to correctly spell Turtle
turt = turtle.Turtle()

scr.bgcolor("seashell")
# changed mispelled liht coral to correctly spell light coral
tColors = ["light salmon", "light sky blue", "pale green", "light coral", "pale turquoise", "plum"]

turt.width(5)
numRings = 6

for i in range(numRings):
    # changed tColors[0] to tColors[i] to actually make it change color
    turt.color(tColors[i])
    radius = 40 * (i + 1)
    turt.up()
    turt.forward(radius)
    turt.down()
    turt.left(90)
    # changed turt.circle(i) to turt.circle(radius) to make big enough circles
    turt.circle(radius)
    # changed the angle to fix the circle's position
    turt.right(90)
    # added parentheses to turt.up so that it would actually take the pen up
    turt.up()
    turt.backward(radius)
    turt.down()

scr.exitonclick()
