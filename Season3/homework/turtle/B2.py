from turtle import *
speed(0.5)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(5) :
    color(colors[i])
    for i in range(2) :
        begin_fill()
        forward(50)
        left(90)
        forward(100)
        left(90)
        end_fill()
    forward(50)
mainloop()