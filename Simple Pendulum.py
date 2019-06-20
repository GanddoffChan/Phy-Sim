from tkinter import *
import time
import math

root = Tk()

W = 100
H = 100
C = Canvas(root, width=W, height=H, background='black')
C.pack()

X = int(W/2)
Y = int(H/2)

t = 0

omega = 0.005

angle = 90

theta = angle*math.pi/180

if X > Y:
    R = Y-10

else:
    R = X-10

r = 5
k = 0.00001
gamma = 0

rate = 0.0000005

while True:
    C.delete("all")
    alpha = -rate*math.sin(theta)-gamma
    omega += alpha
    theta += omega

    gamma = k*omega
    
    x = X + R*math.sin(theta)
    y = Y + R*math.cos(theta)
    C.create_line(x,y, X,Y, fill="white")
    C.create_oval(x-r,y-r, x+r,y+r, fill='white')
    C.update()
    
root.mainloop()



