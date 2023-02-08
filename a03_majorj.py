# Name: Jalen Major

# Github Repository: https://github.com/Berea-College-CSC-226/a03-master-sp23.git

# Google Doc Link: https://docs.google.com/document/d/14IgxBZUsbYPKG8XgFKtPnAnYW6NKLT4UbyrjECMZo8o/edit#

import turtle
wn = turtle.Screen()
hate = turtle.Turtle()
hate.speed(15)
hate.pensize()
wn.colormode(255)
wn.bgcolor(179, 246, 235)
def flower(fnumber):
    for i in range (fnumber):
        hate.pencolor(233, 73, 136)
        hate.circle(190-i, 90)
        hate.lt(90)
        hate.circle(190 - i, 90)
        hate.lt(18)

def roses(rnumber):
    for i in range (rnumber):
        hate.pencolor(48, 116, 68)
        hate.circle(100 - i, 90)
        hate.lt(50)
        hate.circle(100 - i, 90)
        hate.lt(5)

def main ():
    flower(150)
    hate.penup()
    hate.goto(150,200)
    hate.pendown()
    roses(50)
    hate.penup()
    hate.goto(230, -250)
    hate.pendown()
    roses(50)
    hate.penup()
    hate.goto(-90, 150)
    hate.pendown()
    roses(50)
    hate.penup()
    hate.goto(-300, -200)
    hate.pendown()
    roses(50)
    hate.penup()
    hate.goto(0, -200)
    hate.pendown()
    roses(50)


main()

wn.exitonclick()
#comment
