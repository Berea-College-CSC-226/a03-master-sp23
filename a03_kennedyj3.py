from turtle import *

def fleur(): #function
    for i in range(300): #creates the flower
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)

fleur()
mainloop()