from random import *
from turtle import *
bgcolor('dim grey')

##These is the size of the boundary for turtle movement. 
BS = 400

turtle = Turtle()
turtle.shape('turtle')
turtle.pencolor('white')

while True:
    s = randint(0, 100)
    x = randint(0,359)
##To increase the probability of moving forward.    
    θ = (1/90)*(x**2) -4*x +360
    
    turtle.left(θ)
    turtle.forward(s)

    if    (turtle.xcor() < -BS
        or turtle.ycor() < -BS
        or turtle.xcor() > BS
        or turtle.ycor() > BS):

        turtle.left(180)
        turtle.forward(s)    

turtle.mainloop()
