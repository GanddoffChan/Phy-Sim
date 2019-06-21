from tkinter import *

W = 400
H = 500

root = Tk()
root.title('Spring')
C = Canvas(root, width=W, height=H, background='white')
spring = Scale(root, label='k', from_=1,to=10, length=W,
               tickinterval=10, orient=HORIZONTAL)
mass = Scale(root, label='m', from_=1,to=10, length=W,
               tickinterval=10, orient=HORIZONTAL)
length = Scale(root, label='l', from_=100,to=250, length=W,
               tickinterval=10, orient=HORIZONTAL)
gravity = Scale(root, label='g', from_=-1,to=-10, length=W,
               tickinterval=10, orient=HORIZONTAL)
damping = Scale(root, label='c', from_=1,to=10, length=W,
               tickinterval=10, orient=HORIZONTAL)
spring.pack()
mass.pack()
length.pack()
gravity.pack()
damping.pack()
C.pack()

h = 20
v = 0

rate = 10**-5

while True:
    C.delete('all')

    k = spring.get()
    m = mass.get()
    l = length.get()
    g = gravity.get()
    c = damping.get()
    
    Δy = H -l -h
    a = (g +k*Δy/m -c*v/m)*rate
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
