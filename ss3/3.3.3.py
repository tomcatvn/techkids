from turtle import *
def draw_star(x,y,length):
    goto(x,y)
    for _ in range(6):
        forward(length*10)
        rt(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
