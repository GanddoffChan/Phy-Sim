import turtle
import random

arrow = turtle.Turtle()


while True:
    arrow.forward(random.randint(0,10))

    arrow.left(random.randint(-359,359))

turtle.mainloop()


