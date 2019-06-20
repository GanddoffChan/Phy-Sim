from random import *
from turtle import *
bgcolor('dim grey')

##These are the boundaries for turtle movement. 
bx = 400
by = 400

turtle = Turtle()
turtle.shape('turtle')
turtle.pencolor('white')

while True:
    s = randint(0, 100)
    r = randint(0,359)
##To increase the probability of moving forward.    
    θ = (1/90)*(r**2)-4*r+360
    
    turtle.left(θ)
    turtle.forward(s)

    if turtle.xcor() < -bx or turtle.xcor() > bx or turtle.ycor() < -by or turtle.ycor() > by:

        turtle.left(180)
        turtle.forward(s)    

turtle.mainloop()
