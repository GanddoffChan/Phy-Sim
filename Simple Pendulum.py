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
root.title('Simple Pendulum')
C = Canvas(root, width=S, height=S, background='black')
length = Scale(root, label='l', from_=.1*O,to=.9*O, length=S,
               tickinterval=O/10, orient=HORIZONTAL)
gravity = Scale(root, label='g', from_=0,to=-10, length=S,
                tickinterval=1, orient=HORIZONTAL, showvalue=0)
torque = Scale(root, label='τ', from_=-5,to=5, length=S,
                tickinterval=1, orient=HORIZONTAL, showvalue=0)
damping = Scale(root, label='γ', from_=0,to=10, length=S,
                tickinterval=1, orient=HORIZONTAL, showvalue=0)
mass = Scale(root, label='m', from_=1,to=10, length=S,
                tickinterval=1, orient=HORIZONTAL, showvalue=0)
C.pack()
length.pack()
gravity.pack() 
torque.pack() 
damping.pack()
mass.pack()

angle = 30
θ = angle*pi/180
ω = 0
L = 0

while True:
    C.delete('all')
    
    l = length.get()
    g = gravity.get()*10**-4
    τ = torque.get()*10**-2
    γ = damping.get()*10**-2
    m = mass.get()

    I = m*l**2
    L += I*g/l*sin(θ) +τ -sgn(ω)*m*γ*(ω*l)**2
    ω = L/I
    θ += ω
    
    x = O +l*sin(θ)
    y = O +l*cos(θ)
    r = 0.05*O
    
    C.create_line(O,O, x,y, fill='white', width=2)
    C.create_oval(x-r,y-r, x+r,y+r, fill='black',
                  outline='white', width=2)
    C.update()
    
root.mainloop()
