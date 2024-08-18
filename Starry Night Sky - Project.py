from turtle import *
from random import *

speed(0)

bgcolor("black")
hideturtle()

width = window_width()
height = window_height()

# draw_width = - window_width / 2
# draw_height = - window_height / 2
def draw_star(xpos, ypos):
    size = randrange(4, 10)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")
# draw_star(0, 0)

for x in range(100):
    # print("draw_star")
    xpos = randrange(round(-width/2) , round(width/2))
    ypos = randrange(round(-height/2), round(height/2))
    draw_star(xpos, ypos)





# Test area

done()