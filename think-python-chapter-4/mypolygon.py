'''
Documentation, License etc.

@package ThinkPythonChapterFour
'''
from swampy.TurtleWorld import *

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
'2. draw a square'

'0. get the turtle world'

world = TurtleWorld()

'1. get the turtle'

bob = Turtle()

'2. draw a square'

fd(bob, 100)
lt(bob)
fd(bob, 100)
lt(bob)
fd(bob, 100)
lt(bob)
fd(bob, 100)
lt(bob)

print (bob)

wait_for_user()
