from turtle import *

# variables outside functions are also
# known as "global"
diameter = 40
pop_diameter = 100

def draw_balloon():
    color("red")
    dot(diameter)

def inflate_balloon():
    global diameter
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!")
    # If just referrencing a variable
    # then there is no need to specify that
    # a global variable is being used 


    



# Testing area
draw_balloon()
onkey(inflate_balloon, "Up")
listen()
done()