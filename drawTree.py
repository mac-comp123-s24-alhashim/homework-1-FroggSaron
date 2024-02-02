"""
This program creates a tree in the middle of the screen.
The first block creates the trunk.
The second block creates the leaves in a pentagon above the trunk.
The third block creates apples in random positions around the tree's leaves.
The fourth block draws a branch on the right side of the tree.
Author: Sam Jackson email:sjackso2@macalester.edu
"""

import random
import turtle
window = turtle.Screen()
window.bgcolor("light blue")

# This code creates the trunk of the tree
trunk = turtle.Turtle()
trunk.speed(0)
trunk.color("brown")
trunkLength = [50, 300, 50, 300]
trunk.penup()
trunk.goto(0,-300)
trunk.pendown()
trunk.begin_fill()
for i in range(4):
    trunk.forward(trunkLength[i])
    trunk.left(90)
trunk.end_fill()

# This code creates the leaves of the tree
leaves = turtle.Turtle()
leaves.speed(0)
leaves.color("dark green")
leaves.penup()
leaves.goto(-75,0)
leaves.pendown()
leaves.begin_fill()
for i in range(5):
    leaves.forward(200)
    leaves.left(72)
leaves.end_fill()

# This code creates apples on the tree
apples = turtle.Turtle()
apples.speed(0)
apples.color("red")
for i in range(15):
    apples.penup()
    apples.goto(random.randint(-100,100), random.randint(0,200))
    apples.pendown()
    apples.begin_fill()
    apples.circle(10)
    apples.end_fill()
# This code creates a branch on the tree
branch = turtle.Turtle()
branch.speed(0)
branch.color("brown")
branch.penup()
branch.goto(50,-100)
branch.pendown()
branch.begin_fill()
branch.forward(100)
branch.right(170)
branch.forward(100)
branch.end_fill()

window.exitonclick()