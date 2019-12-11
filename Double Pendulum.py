from tkinter import *
from math import *

def sgn(x):
    if x > 0:
        return(1)
    elif x < 0:
        return(-1)
    return(0)

S = 1000
O = S/2
root = Tk()
root.title('Simple Pendulum')
C = Canvas(root, width=S, height=S, background='black')

length1 = Scale(root, label='l1', from_=.1*O,to=.5*O,
               tickinterval=O/50, orient=VERTICAL)
length2 = Scale(root, label='l2', from_=.1*O,to=.5*O,
               tickinterval=O/50, orient=VERTICAL)
mass1 = Scale(root, label='m1', from_=1,to=10, length=S, resolution=-1,
                tickinterval=1, orient=VERTICAL, showvalue=1)
mass2 = Scale(root, label='m2', from_=1,to=10, length=S, resolution=-1,
                tickinterval=1, orient=VERTICAL, showvalue=1)
gravity = Scale(root, label='g', from_=0,to=-10, length=S,
                tickinterval=1, orient=VERTICAL, showvalue=0)
damping = Scale(root, label='γ', from_=0,to=10, length=S,
                tickinterval=1, orient=VERTICAL, showvalue=0)

C.pack()
length1.pack()
length2.pack()
mass1.pack()
mass2.pack()
gravity.pack()
damping.pack()
length1.place(bordermode=OUTSIDE, height=S, width=100, x=0, y=0)
length2.place(bordermode=OUTSIDE, height=S, width=100, x=100, y=0)
mass1.place(bordermode=OUTSIDE, height=S, width=100, x=1920-200, y=0)
mass2.place(bordermode=OUTSIDE, height=S, width=100, x=1920-100, y=0)
gravity.place(bordermode=OUTSIDE, height=S, width=100, x=1920-300, y=0)
damping.place(bordermode=OUTSIDE, height=S, width=100, x=200, y=0)

angle1 = 30
angle2 = 90
θ1 = angle1*pi/180
θ2 = angle2*pi/180
ω1 = 0
ω2 = 0


while True:
    C.delete('all')
    
    g = gravity.get()*10**-4
    γ = damping.get()*10**-1
    
    l1 = length1.get()
    m1 = mass1.get()
    l2 = length2.get()
    m2 = mass2.get()

    N1 = g*(2*m1+m2)*sin(θ1)+m2*g*sin(θ1-2*θ2)-2*sin(θ1-θ2)*m2*(ω2**2*l2+ω1**2*l1*cos(θ1-θ2))
    D1 = l1*(2*m1+m2-m2*cos(2*θ1-2*θ2))
    N2 = 2*sin(θ1-θ2)*(ω1**2*l1*(m1+m2)-g*(m1+m2)*cos(θ1)+ω2**2*l2*m2*cos(θ1-θ2))
    D2 = l2*(2*m1+m2-m2*cos(2*θ1-2*θ2))
    
    α1 = N1/D1 -sgn(ω1)*γ*ω1**2
    α2 = N2/D2 -sgn(ω2)*γ*ω2**2
    ω1 += α1
    ω2 += α2
    θ1 += ω1
    θ2 += ω2
    
    x1 = O +l1*sin(θ1)
    y1 = O +l1*cos(θ1)
    x2 = x1 +l2*sin(θ2)
    y2 = y1 +l2*cos(θ2)
    r1 = m1**3/10
    r2 = m2**3/10
    
    C.create_line(O,O, x1,y1, fill='white', width=2)
    C.create_oval(x1-r1,y1-r1, x1+r1,y1+r1, fill='white')
    C.create_line(x1,y1, x2,y2, fill='white', width=2)
    C.create_oval(x2-r2,y2-r2, x2+r2,y2+r2, fill='white')
    C.update()
    
root.mainloop()
