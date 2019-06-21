from tkinter import *
import time

W = 400
H = 900

root = Tk()
root.title('Spring')
C = Canvas(root, width=W, height=H, background='white')
C.pack()

k = 10
m = 10
l = 450
h = 400
g = -9.81
v = -0.1

rate = 10**-5

while True:
    C.delete('all')

    Δy = H -l -h
    a = (g +k*Δy/m)*rate
    
    v += a
    h += v

    x = W/2
    y = H -h
    w = 200

    C.create_line(x-w/2,y, x+w/2,y, width=2)
    C.create_line(x-w/2,H, x+w/2,H, width=2)
    C.create_line(x-w/2,y, x+w/2,(H+y)/2, width=2)
    C.create_line(x+w/2,(H+y)/2, x-w/2,H, width=2)
    C.update()

root.mainloop()    

    
