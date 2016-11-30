from turtle import *
goc_re = 0


for canh in range(4,10):
    goc_re = 360/canh
    for doi_mau in range(canh):
        
        if doi_mau % 2 == 0:
             color("red")
        if doi_mau % 2 == 1:
             color("blue")
        forward(100)
        lt(goc_re)
        
        
            
