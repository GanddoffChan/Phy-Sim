from tkinter import *
from math import *

S = 500
O = S/2
r = 0.05*O

root = Tk()
C = Canvas(root, width=S, height=S, background='black')
length = Scale(root, label='L', from_=.1*O,to=.9*O, length=S, tickinterval=50, orient=HORIZONTAL)
damping = Scale(root, label='γ', from_=0,to=100, length=S, tickinterval=50, orient=HORIZONTAL)
C.pack()
length.pack()
damping.pack()

ω = 1*10**-5
angle = 180
θ = angle*pi/180
g = 5*10**-5

while True:
    C.delete('all')

    L = length.get()
    γ = damping.get()*10**-6
    
    α = -g/L*sin(θ) -γ*ω
    ω += α
    θ += ω
    
    x = O + L*sin(θ)
    y = O + L*cos(θ)
    
    C.create_line(x,y, O,O, fill='white', width=2)
    C.create_oval(x-r,y-r, x+r,y+
                  r, fill='black', outline='white', width=2)
    C.update()
    
root.mainloop()
