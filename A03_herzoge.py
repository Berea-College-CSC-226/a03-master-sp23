################################################################################
# Name: Eli Herzog
# Username: Herzoge
# Repo link: https://github.com/Berea-College-CSC-226/a03-master-sp23.git
# Google Doc link: https://docs.google.com/document/d/1OtzO6C-OpJJT-QPJNbTZWNtCtBfOBBc6-Wujg3FPHWk/edit?usp=sharing
########################################################################################
import turtle

wn = turtle.Screen()
salt = turtle.Turtle() ## my turtle is called salt
screen = turtle.Screen()
screen.bgcolor(.2518, .3961, .2562) #set bg color
turtle.speed("slow") #set speed



def first(): #this code draws the shaker
    turtle.fillcolor(.4012, .434, .3552)
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(160)
    turtle.left(110)
    turtle.forward(150)
    turtle.left(70)
    turtle.forward(60)
    turtle.left(70)
    turtle.forward(150)
    turtle.end_fill()

def second(): #this code draws the salt
    turtle.fillcolor(.76, .7978, .6598)
    turtle.begin_fill()
    turtle.left(110)
    turtle.forward(163)
    turtle.left(110)
    turtle.forward(50)
    turtle.left(70)
    turtle.forward(129.5)
    turtle.left(70)
    turtle.forward(50)
    turtle.left(110)
    turtle.forward(163)
    turtle.left(110)
    turtle.forward(50)
    turtle.end_fill()

def third(): #this code draws the cap
    turtle.fillcolor(.3264, .3478, .2799)
    turtle.forward(100)
    turtle.begin_fill()
    turtle.right(20)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.end_fill()

def fourth(): #this code draws the top of the cap
    turtle.fillcolor(.2143, .2287, .1825)
    turtle.begin_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown()
    turtle.circle(30, -180)
    turtle.end_fill()


def fifth(): #this code draws the text
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(100)
    # turtle.pendown()
    turtle.write("Salt", True, align="center")
    wn.exitonclick()

def main()
    first()
    second()
    third()
    fourth()
    fifth()

main()