"""
Determines where to place a circle in a given area, finds the diameter of the largest circle need
to search the area, and figures out how many circles the rescue drone would need to fly.
@author: Sam Jackson (sjackso2@macalester.edu)
"""
import math
# Asks user the dimensions of the rectangular area the drone will search and assigns it to an integer variable
width = int(input("What is the width in meters of the search area:"))
length = int(input("What is the length in meters of the search area:"))

# Calculates the centerpoint of the search area
centerpointx = width / 2
centerpointy = length / 2
# Finds the radius of the circle that the drone uses
diameter = math.sqrt((centerpointx ** 2) + (centerpointy ** 2))
radius = diameter / 2
# Prints the radius
print(radius)
# Finds how many circles the drone will have to make rounded to the largest integer
circleNum = radius / 5
circleNum = math.ceil(circleNum)
# Prints the number of circles
print(circleNum)
