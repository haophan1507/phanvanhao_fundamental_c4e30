from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(0.5)
color(colors[0])
for i in range(3) :
    forward(100)
    left(120)
color(colors[1])
for i in range(4) :
    forward(100)
    left(90)
color(colors[2])
for i in range(5) :
    forward(100)
    left(72)
color(colors[3])
for i in range(6):
    forward(100)
    left(60)
color(colors[4])
for i in range(7) :
    forward(100)
    left(360/7)
mainloop()