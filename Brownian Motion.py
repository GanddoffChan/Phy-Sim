from random import *

from turtle import *
bgcolor('dim grey')


particle = Turtle()

particle.shape('turtle')

particle.pencolor('white')


while True:
    particle.forward(randint(0,25))

    particle.left(randint(-359,359))

turtle.mainloop()
