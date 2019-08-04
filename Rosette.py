# RosetteGoneWild.py
# Billy Ridgeway
# Creates a rosette pattern.

import turtle           # Imports turtle graphics.
t = turtle.Pen()        # Creates a new turtle called t.
turtle.bgcolor("white") # Sets the background color to white.



for x in range(4):      # The range equals how many times it will draw a circle.
    t.circle(100)       # Sets the size of the circles.
    t.left(90)          # How many degrees the circle will shift to the left.
