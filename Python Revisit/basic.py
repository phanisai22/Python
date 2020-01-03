import turtle
import sys

friend_turtle = turtle.Turtle()

# friend_turtle.forward(100)
# friend_turtle.right(90)
# friend_turtle.forward(100)
# friend_turtle.right(90)
# friend_turtle.forward(100)
# friend_turtle.right(90)
# friend_turtle.forward(100)
# friend_turtle.right(90)

# ===========================================
# Functions

def create_square():
    for i in range(4):
        friend_turtle.forward(100)
        friend_turtle.right(90)

create_square()
friend_turtle.forward(200)
create_square()

turtle.done()