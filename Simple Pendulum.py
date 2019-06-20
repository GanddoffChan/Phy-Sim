from tkinter import *
from math import *

root = Tk()

W = 500
H = 500
C = Canvas(root, width=W, height=H, background='black')
C.pack()

X = int(W/2)
Y = int(H/2)

t = 0

omega = 0.002

angle = 90

theta = angle*pi/180

if X > Y:
    R = 0.9*Y

else:
    R = 0.9*X

r = 0.05*R
k = 0.00001
gamma = 0

rate = 0.0000005

while True:
    C.delete("all")
    alpha = -rate*sin(theta)-gamma
    omega += alpha
    theta += omega

    gamma = k*omega
    
    x = X + R*sin(theta)
    y = Y + R*cos(theta)
    C.create_line(x,y, X,Y, fill="white")
    C.create_oval(x-r,y-r, x+r,y+r, fill='white')
    C.update()
    
root.mainloop()
