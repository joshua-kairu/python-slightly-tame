'''
Documentation, License etc.

@package ThinkPythonChapterFour
'''
from TurtleWorld import *
from math import pi

'''
Function to draw a square with a given length

@param turtle A Turtle
@param length The length of the square
'''
def square(turtle, length):
    for i in range(4):
        fd(turtle, length)
        lt(turtle)
        
'''
Function to draw a regular polygon with a given length

@param turtle A Turtle
@param length The length of the polygon
@param sides The number of sides the polygon will have
'''
def polygon(turtle, length, sides):
    
    '0. get polygon angle'
    '1. draw the polygon'
    
    '0. get polygon angle'
    
    angle=360.0/sides
    print(angle)
    
    '1. draw the polygon'

    for i in range(sides):
        fd(turtle, length)
        lt(turtle, angle)

'''
Draws a circle given a radius

@param turtle A Turtle
@param radius The radius
'''
def circle(turtle, radius):

        "0. get the circle's circumference"
        '1. decide the number of sides using length * sides = circumference'
        '2. draw the circle'
        
        "0. get the circle's circumference"
        
        circumference = 2 * pi * radius
        
        '1. decide the number of sides using length * sides = circumference'
        
        length=5
        sides = int(circumference/length)
        
        '2. draw the circle'
        
        polygon(turtle,length,sides)


'''
fd - forward
bk - backward
lt - left turn
rt - right turn
pu - pen up
pd - pen down
'''

'0. get the turtle world'
'1. get the turtle'
'1a. make him fast'
'2. draw a square with given length'
'3. draw a polygon with given length and sides'
'4. draw a circle with given radius'

'0. get the turtle world'

world = TurtleWorld()

'1. get the turtle'

bob = Turtle()

'1a. make him fast'

bob.delay=0.01

'2. draw a square with given length'

#square(bob, 50)

'3. draw a polygon with given length and sides'

#polygon(bob, 25, 20)

'4. draw a circle with given radius'

circle(bob,10)

wait_for_user()

