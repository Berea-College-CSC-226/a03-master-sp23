################################################################################
# Name: Nadia Barkovska
# Username: barkovskan
# Repo link: https://github.com/Berea-College-CSC-226/a03-master-sp23.git
# Google Doc link: https://docs.google.com/document/d/1INkbRnrG_kgYI2vmMaR855kbun6MNhkOauSThRKHzjo/edit?usp=sharing
########################################################################################

import turtle
import math


wn = turtle.Screen()
kiwi= turtle.Turtle() ##### kiwi is the name of the turtle
screen= turtle.Screen()
screen.bgcolor("lavenderblush")

def main():
    #used this to define the main attributes
    kiwi.color("black")
    kiwi.shape("square")
    kiwi.speed(2)

# now i will start drawing the base of the house

kiwi.fillcolor("bisque3")
kiwi.begin_fill()
kiwi.right(90)
kiwi.forward(150)
kiwi.left(90)
kiwi.forward(220)
kiwi.left(90)
kiwi.forward(150)
kiwi.left(90)
kiwi.forward(220)
kiwi.right(90)
kiwi.end_fill()

# now i will be drawing the roof

kiwi.fillcolor("bisque4")
kiwi.begin_fill()
kiwi.right(45)
kiwi.forward(150)
kiwi.right(90)
kiwi.forward(150)
kiwi.end_fill()

# I will now draw a window
kiwi.fillcolor("yellow")
kiwi.begin_fill()
kiwi.right(90)
kiwi.penup()
kiwi.forward(100)
kiwi.right(45)
kiwi.pendown()
kiwi.forward(90)
kiwi.right(90)
kiwi.forward(60)
kiwi.right(90)
kiwi.forward(90)
kiwi.right(90)
kiwi.forward(60)
kiwi.end_fill()
