from turtle import *
def draw_square(length,color):
    pencolor(color)
    for _ in range(4):
        
        rt(90)
        forward(length*5)
        
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

        
