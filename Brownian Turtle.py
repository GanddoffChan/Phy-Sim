from random import *
from turtle import *

##Thisis the size of the boundary for turtle movement. 
BS = 400

turtle = Turtle()
turtle.shape('turtle')
bgcolor('dim grey')
turtle.color('dark green')
turtle.pencolor('light green')

while True:
    s = randint(0,100)
    x = randint(1,359)
    n = 2
##To increase the probability of moving forward.
    θ = 360*(x-180)**(2*n-1)/(180**(2*n-1))
    
    turtle.left(θ)
    turtle.forward(s)

    if    (turtle.xcor() < -BS
        or turtle.ycor() < -BS
        or turtle.xcor() > BS
        or turtle.ycor() > BS):

        turtle.left(180)
        turtle.forward(s)    

turtle.mainloop()
