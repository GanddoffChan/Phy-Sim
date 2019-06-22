from tkinter import *
from math import *

def sgn(x):
    if x > 0:
        return(1)
    elif x < 0:
        return(-1)
    return(0)

S = 666
O = S/2
root = Tk()
root.title('Angular Momentum')
C = Canvas(root, width=S, height=S, background='black')
torque = Scale(root, label='τ', from_=-5,to=5, length=S,
                tickinterval=1, orient=HORIZONTAL, showvalue=0)
radius = Scale(root, label='r', from_=.1*O,to=.7*O, length=S,
               tickinterval=.7*O -.01*O, orient=HORIZONTAL)
mass = Scale(root, label='m', from_=1,to=10, length=S,
                tickinterval=1, orient=HORIZONTAL, showvalue=0)
damping = Scale(root, label='γ', from_=0,to=10, length=S,
                tickinterval=1, orient=HORIZONTAL, showvalue=0)
C.pack()
torque.pack()
radius.pack()
mass.pack()
damping.pack()

L = 0
ω = 0
θ = 0

while True:
    C.delete('all')
    
    r = radius.get()
    τ = torque.get()*10**-6
    m = mass.get()
    γ = damping.get()*10**-2

    I = r**2*m
    L += I*(τ -sgn(ω)*γ*(ω*r)**2)
    ω = L/I
    θ += ω
    
    l = 100
    w = 50

    x1 = O +(r+ w/2)*cos(θ)
    y1 = O -(r+ w/2)*sin(θ)
    x2 = O -(r+ w/2)*cos(θ)
    y2 = O +(r+ w/2)*sin(θ)

    xul1 = x1 +l/2*sin(θ)
    yul1 = y1 +l/2*cos(θ)
    xur1 = x1 -l/2*sin(θ)
    yur1 = y1 -l/2*cos(θ)
    xlr1 = xur1 +w*cos(θ)
    ylr1 = yur1 -w*sin(θ)
    xll1 = xul1 +w*cos(θ)
    yll1 = yul1 -w*sin(θ)

    xul2 = x2 -l/2*sin(θ)
    yul2 = y2 -l/2*cos(θ)
    xur2 = x2 +l/2*sin(θ)
    yur2 = y2 +l/2*cos(θ)
    xlr2 = xur2 -w*cos(θ)
    ylr2 = yur2 +w*sin(θ)
    xll2 = xul2 -w*cos(θ)
    yll2 = yul2 +w*sin(θ)
    
    C.create_line(x1,y1, x2,y2, fill='white', width=2)
    C.create_polygon(xul1,yul1, xur1,yur1, xlr1,ylr1, xll1,yll1,
                     fill='black',outline='white', width=2)
    C.create_polygon(xul2,yul2, xur2,yur2, xlr2,ylr2, xll2,yll2,
                     fill='black', outline='white', width=2)
    C.update()
    
root.mainloop()

