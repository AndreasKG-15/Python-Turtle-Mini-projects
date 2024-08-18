from turtle import *


# Functions are a block of reusable code

# print("Hello Bob")
# print("Hello Steve")
# print("Hello Mary")

def say_hello (name):
    print("How are you " + name)

say_hello("Bob")
say_hello("Steve")
say_hello("Mary")
say_hello("Rob")

def move_and_turn(distance, angle):
    forward(distance)
    right(angle)
    print("print to the console")

# The lines of code calling the function
# cannot run before the function is created
# because it would then be calling nothing 
move_and_turn(100, 45)
move_and_turn(50, 90)

# brackets usually mean you are calling a function
# pre-configured or not


done()