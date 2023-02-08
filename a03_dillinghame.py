######################################################################
# Author: Emily Dillingham
# Username: dillinghame
# Assignment: A03 Functional Turtles
# Purpose:
######################################################################
# Acknowledgements:
#
# Found colors from: https://trinket.io/docs/colors
######################################################################

import turtle

def move(t,x,y):   # this function allows me to move the turtle around as I need to to draw things in different locations
    t.penup()
    t.goto(x,y)
    t.pendown()

def rectangle(t,length,height):   # this simply creates a rectangle and allows for different lengths and heights (could make a square if length=height)
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(height)
        t.left(90)

def triangle(t,bottom,sides): # creates a triangle
    t.left(30)
    t.forward(sides)
    t.right(60)
    t.forward(sides)
    t.right(150)
    t.forward(bottom)


def house(t):   #makes the base, roof, and chimney of the house
    t.fillcolor('#4682B4')
    t.begin_fill()
    rectangle(t,400,300)  # base
    t.end_fill()
    t.fillcolor('#D2691E')
    move(t,100,150)
    t.begin_fill()
    rectangle(t,50,80)   # base of chimney
    t.end_fill()
    move(t,90,230)
    t.begin_fill()
    rectangle(t,70,20)    # top of chimney
    t.end_fill()
    move(t,-200,150)
    t.begin_fill()
    triangle(t,400,230)   # roof
    t.end_fill()

def panes(t,height,width):  # draws lines in a cross shape with variable lengths, this allows me to make the windows look like they have panes
    t.penup()
    t.forward(width/2)
    t.left(90)
    t.pendown()
    t.forward(height)
    t.penup()
    t.backward(height/2)
    t.left(90)
    t.forward(width/2)
    t.left(180)
    t.pendown()
    t.forward(width)
    t.penup()
    t.right(90)
    t.forward(height/2)
    t.left(90)
    t.pendown()

def flower(t,color,x,y):  # makes a flower
    t.pensize(3)
    t.color('#008000')
    move(t,x,y)
    t.left(90)
    t.forward(20)
    t.color('#FFFF00')
    t.dot(5)
    t.color(color)
    move(t,x-4,y+20)
    t.dot(5)
    move(t,x,y+23)
    t.dot(5)
    move(t,x+4,y+20)
    t.dot(5)
    move(t,x+3,y+16)
    t.dot(5)
    move(t,x-3,y+16)
    t.dot(5)
    move(t,x,y)
    t.right(90)

def main():  # draws everything
    wn = turtle.Screen()  # this block creates the screen and turtle and sets their attributes
    wn.bgcolor('#98FB98')
    tess = turtle.Turtle()
    tess.pencolor("#000000")
    tess.pensize(5)
    tess.speed(10)

    move(tess,-200,-150)  # this block makes the house with all the details minus the flowers and turtles
    house(tess)
    tess.left(180)
    move(tess,-150,0)
    tess.fillcolor('#FFFFFF')    # this is where the windows start
    tess.begin_fill()
    rectangle(tess,50,75)
    tess.end_fill()
    panes(tess,75,50)
    move(tess,100,0)
    tess.begin_fill()
    rectangle(tess,50,75)
    tess.end_fill()
    panes(tess,75,50)
    move(tess,-175,-145)
    tess.fillcolor('#8B4513')    # this is where the flower boxes are made
    tess.begin_fill()
    rectangle(tess,100,50)
    tess.end_fill()
    move(tess,75,-145)
    tess.begin_fill()
    rectangle(tess,100,50)
    tess.end_fill()
    move(tess,-45,-150)
    tess.fillcolor('#000000')
    tess.begin_fill()
    rectangle(tess,90,200)    # this makes the door
    tess.end_fill()
    move(tess,30,-40)
    tess.shape('circle')
    tess.pencolor('#FFD700')
    tess.fillcolor('#FFD700')
    tess.pensize(2)
    tess.stamp()               # this is the doorknob

    x=-184  # these next two blocks make the flowers in the flower boxes
    for colors in ['#800080','#FFFFFF','#F08080','#FF0000','#FF4500','#800080','#FFFFFF','#F08080','#FF0000','#FF4500']:
        x = x+11
        y = -95
        flower(tess,colors,x,y)

    x=65
    for colors in ['#800080','#FFFFFF','#F08080','#FF0000','#FF4500','#800080','#FFFFFF','#F08080','#FF0000','#FF4500']:
        x = x+11
        y = -95
        flower(tess,colors,x,y)

    move(tess,-190,-145)  # this block adds little turtle friends at the bottom corners of the house :)
    tess.shape('turtle')
    tess.color('#008000')
    tess.stamp()
    move(tess,190,-145)
    tess.right(180)
    tess.stamp()


    wn.exitonclick()

main()