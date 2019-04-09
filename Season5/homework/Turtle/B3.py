from turtle import *
def draw_square(a,b) :
    color(a)
    for i in range(4) :
        forward(b)
        left(90)
    mainloop()
l = int(input('Nhap chieu dai :'))
c = str(input('Nhap mau sac :'))
draw_square(c,l)