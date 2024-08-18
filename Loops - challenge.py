from turtle import *

def move_and_turn(angle):
    forward(50)
    right(angle)

'''
move_and_turn(45)
move_and_turn(45)
move_and_turn(45)
move_and_turn(45)
move_and_turn(45)
move_and_turn(45)
move_and_turn(45)
move_and_turn(45)
'''
# Tedious ^
for x in range(8):
    move_and_turn(45)
# Octagon ^
clear()
for x in range(12):
    move_and_turn(30)
# Dodecagon ^

# Test area
done()

'''
Different kinds of loops
1. for loops
    runs a set amount of times
2. while loops
    runs as long as a given condition is true

the "break" command will automatically end the loop and then continue
'''
