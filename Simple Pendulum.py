from tkinter import *
from math import *

root = Tk()
W = 500
H = 500
C = Canvas(root, width=W, height=H, background='black')
C.pack()

X = int(W/2)
Y = int(H/2)

if X > Y:
    R = .9*Y

else:
    R = .9*X

r = 0.05*R    

ω = 2*10**-3

angle = 90
θ = angle*pi/180

γ = 1*10**-5

rate = 5*10**-7

while True:
    C.delete('all')
    
    α = -rate*sin(θ)-γ*ω
    ω += α
    θ += ω
    
    x = X + R*sin(θ)
    y = Y + R*cos(θ)
    
    C.create_line(x,y, X,Y, fill="white")
    C.create_oval(x-r,y-r, x+r,y+r, fill='white')
    C.update()
    
root.mainloop()
