################################################################################
# Username: jjjonesj
#
# Assignment: Fully Functional Gitty Psychedelic Robotic Turtles
# 2/7/2023
#################################################################################
import turtle
w = turtle.Screen()
w.bgcolor("#FFA0AC")

####################### Making A Very Much Adequete Home #####################################

# Turtle variables for various functions #

a = turtle.Turtle()
a.pensize(10)
a.speed(0)
a.color("#F6BDD1")

b = turtle.Turtle()
b.pensize(10)
b.speed(0)
b.color("#FFA5C5")

c = turtle.Turtle()
c.pensize(10)
c.speed(0)
c.color("#F4F4F4")

# Function for moving turtles to specific places without too much hassle
def move(p,x,y):
    p.penup()
    p.goto(x,y)
    p.pendown()

move(a,-200,210)
# Base structure for hotel/ side parts
def base(pp,pp1,pp2):
    for i in range(2):
        pp.begin_fill()
        pp.forward(pp1) #go forward 400 for og base
        pp.right(90)
        pp.forward(pp2) #go forward 500 for og base
        pp.right(90)
        pp.end_fill()
# door
def door():
    move(b,-50,-90)
    base(b,90,200)
# porch
def porch():
    move(c,-80,-70)
    base(c,150,10)
    move(c,-60,-80)
    base(c,5,230)
    move(c,40,-80)
    base(c,5,230)
    move(c,-220,-300)
    base(c,440,10)
# That thing at the top of city buildings, it may be an air-conditioning unit
def s():
    move(c,-210,240)
    base(c,200,-50)


# Windows
def win():
    for i in range(3):
        c.penup()
        c.forward(120)
        c.pendown()
        base(c,70,90)
# Roof Portions
def roof():
    move(b,-220,230)
    base(b,440,10)


def main():
    #base of hotel
    base(a,400,500)
    #roof
    roof()
   #windows
    move(c, -280, 50)
    win()
    move(c, -280, 170)
    win()
    #door
    door()
    #Not sure what the actual name for it would be so, its just extra stuff for the door
    porch()
    #air conditioning unit- maybe
    s()
    a.hideturtle()
    b.hideturtle()
    c.hideturtle()
    w.exitonclick()
main()


