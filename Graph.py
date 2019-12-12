from tkinter import *
import math

def sin(x):
    return(math.sin(x))
def cos(x):
    return(math.cos(x))
def tan(x):
    return(math.tan(x))


def sec(x):
    return(1/cos(x))
def cosec(x):
    return(1/sin(x))
def cot(x):
    return(1/tan(x))
def ln(x):
    return(math.log(x))

    

W = 1000
H = 900
O_x = W/2
O_y = H/2
root = Tk()
root.title('Graph')
C = Canvas(root, width=W, height=H, background='black')
C.pack()

exponent = Scale(root, label='n', from_=-10,to=10, length=W, orient=HORIZONTAL)
exponent.pack()

C.create_line(0,O_y, W,O_y, fill='grey', width=1)
C.create_line(W-20,O_y+-20, W,O_y, fill='grey', width=1)
C.create_line(W-20,O_y+20, W,O_y, fill='grey', width=1)
C.create_line(O_x,0, O_x,H, fill='grey', width=1)
C.create_line(O_x,0, O_x-20,20, fill='grey', width=1)
C.create_line(O_x,0, O_x+20,20, fill='grey', width=1)
C.create_oval(O_x-12,O_y+10, O_x-28,O_y+30, fill='black', outline='grey') 

r_x = 40
r_y = 40
x_zoom = W/r_x
y_zoom = H/r_y
X = O_x/x_zoom
x = -X
dx = 1


C.create_line(O_x*(1+0.2/r_x),O_y-10, O_x*(1+0.2/r_x),O_y+10, fill='grey', width=1)
C.create_line(O_x*(1+2/r_x),O_y-10, O_x*(1+2/r_x),O_y+10, fill='grey', width=1)
C.create_line(O_x*(1+20/r_x),O_y-10, O_x*(1+20/r_x),O_y+10, fill='grey', width=1)
C.create_line(O_x-10, O_y*(1-0.2/r_y), O_x+10, O_y*(1-0.2/r_y), fill='grey', width=1)
C.create_line(O_x-10, O_y*(1-2/r_y), O_x+10, O_y*(1-2/r_y), fill='grey', width=1)
C.create_line(O_x-10, O_y*(1-20/r_y), O_x+10, O_y*(1-20/r_y), fill='grey', width=1)

while True:

    n = exponent.get()
    
    def F(x):
        return(x**n)

    def f(x):
        return(n*x**(n-1))

    if x > X:
            x = -X

    else:
        x += dx/x_zoom
        
        y = O_y-y_zoom*F(x)
        dy = f(x)*dx*y_zoom/x_zoom
        
        C_id = C.create_line(x*x_zoom-dx+O_x,y+dy, x*x_zoom+dx+O_x,y-dy, fill='white')
        C.after(1000, C.delete, C_id)
        C.update()

root.mainloop()
