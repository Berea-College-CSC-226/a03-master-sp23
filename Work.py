######################################################################
# Author: David Brothers             TODO: Change this to your name, if modifying
# Username: brothersd                      TODO: Change this to your username, if modifying#
# Assignment: A0  oustrophedon Turtles
# Purpose: To demonstrate the turtle library and loops
######################################################################
# Acknowledgements:
#
# original from http://interactivepython.org/runestone/static/thinkcspy/index.html
# first modified by Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#Google doc linkhttps://docs.google.com/document/d/1hQpibEoP1PHOIVsonx8yFGzPDqkq2h-yM4mXgyRGuUw/edit#
######################################################################

import turtle

wn= turtle.Screen()
turtle= turtle.Turtle()
wn.colormode(255)
wn.bgcolor(10, 32, 69)
turtle.pencolor()


def bun(x): # Makes first bun
    turtle.begin_fill()
    turtle.forward(30)
    for i in range(2):
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
    turtle.fillcolor(255,160,122)
    turtle.end_fill()

def meat(): # makes meat
    turtle.begin_fill()
    turtle.fillcolor(208,95,92)
    turtle.left(120)
    turtle.forward(20)
    turtle.right(70)
    turtle.forward(30)
    turtle.right(50)
    turtle.forward(80)
    turtle.right(70)
    turtle.forward(30)
    turtle.right(70)
    turtle.forward(20)
    turtle.end_fill()
    turtle.right(70)
    turtle.penup()
    turtle.forward(85)
    turtle.right(150)
    turtle.down()
def onions(): # makes Cheese
    turtle.begin_fill()
    turtle.fillcolor(255,165,0)
    for i in range(2):
        turtle.forward(80)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)

    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.fillcolor(255, 90, 100)
    turtle.end_fill()

def bunn(): # Makes second bunn
    turtle.begin_fill()
    turtle.fillcolor(255,160,122)
    turtle.forward(-10)
    turtle.forward(100)
    turtle.left(90)

    for i in range(10):
        turtle.forward(3)
        turtle.left(90)
        turtle.forward(3)
        turtle.right(90)
    turtle.left(90)
    turtle.forward(50)

    for i in range(10):
        turtle.forward(3)
        turtle.left(90)
        turtle.forward(3)
        turtle.right(90)
    turtle.forward(-10)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(90)

def Burger(x):      #Makes Borger
        bun(x)
        meat()
        onions()
        bunn()

def main():
    Burger(0)
    Burger(30)
    Burger(-40)
    Burger(180)
main()
wn.exitonclick()

