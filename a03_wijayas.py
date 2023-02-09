########################################################################################################################
# Authors: Syakira Wijaya
# Username: wijayas
#
# Assignment: A03 Functional Turtles
# Google Doc Link: https://docs.google.com/document/d/18CzJoGAvDcTwbfTjFG658ARHFs3EzJyYPNzlKRVbwt4/edit?usp=sharing
########################################################################################################################

import turtle

def rectangle(shape, width, height):
    """
    Creating a rectangle shape
    :param shape: turtle
    :param width: width
    :param height: height
    :return: none
    """
    for i in range(2):
        shape.forward(width)
        shape.left(90)
        shape.forward(height)
        shape.left(90)

def drawWindow(turt):
    """
    Creating 3 windows in a row
    :param turt: turtle
    :return: none
    """
    for windows in range(3):
        turt.begin_fill()
        for i in range (2):
            turt.forward(20)
            turt.left(90)
            turt.forward(30)
            turt.left(90)
        turt.end_fill()
        turt.penup()
        turt.forward(60)
        turt.pendown()

def main():
    wn = turtle.Screen()
    wn.bgcolor("#87CEFA")

    #draw the main apartment building
    building = turtle.Turtle()
    building.hideturtle()
    building.pensize(5)
    building.pencolor("#000000")
    building.fillcolor("#D3D3D3")
    building.begin_fill()
    building.penup()
    building.setpos(0, -50)
    building.pendown()
    rectangle(building, 200, 400)
    building.end_fill()

    #draw window row 1 to 6
    bwindow = turtle.Turtle()
    bwindow.hideturtle()
    bwindow.pensize(2)
    bwindow.pencolor('#87CEEB')
    bwindow.fillcolor('#87CEEB')
    bwindow.speed(0)
    bwindow.penup()
    bwindow.setpos(30, 50)
    bwindow.pendown()
    drawWindow(bwindow)

    bwindow = turtle.Turtle()
    bwindow.hideturtle()
    bwindow.pensize(2)
    bwindow.pencolor('#87CEEB')
    bwindow.fillcolor('#87CEEB')
    bwindow.speed(0)
    bwindow.penup()
    bwindow.setpos(30, 110)
    bwindow.pendown()
    drawWindow(bwindow)

    bwindow = turtle.Turtle()
    bwindow.hideturtle()
    bwindow.pensize(2)
    bwindow.pencolor('#87CEEB')
    bwindow.fillcolor('#87CEEB')
    bwindow.speed(0)
    bwindow.penup()
    bwindow.setpos(30, 170)
    bwindow.pendown()
    drawWindow(bwindow)

    bwindow = turtle.Turtle()
    bwindow.hideturtle()
    bwindow.pensize(2)
    bwindow.pencolor('#87CEEB')
    bwindow.fillcolor('#87CEEB')
    bwindow.speed(0)
    bwindow.penup()
    bwindow.setpos(30, 230)
    bwindow.pendown()
    drawWindow(bwindow)

    bwindow = turtle.Turtle()
    bwindow.hideturtle()
    bwindow.pensize(2)
    bwindow.pencolor('#87CEEB')
    bwindow.fillcolor('#87CEEB')
    bwindow.speed(0)
    bwindow.penup()
    bwindow.setpos(30, 290)
    bwindow.pendown()
    drawWindow(bwindow)

    #draw the apartment entrance door
    door = turtle.Turtle()
    door.hideturtle()
    door.pensize(3)
    door.pencolor("#696969")
    door.fillcolor("#A9A9A9")
    door.speed(0)
    door.penup()
    door.setpos(70,-50)
    door.pendown()
    door.begin_fill()
    rectangle(door, 30, 50)
    door.penup()
    door.setpos(100,-50)
    door.pendown()
    rectangle(door, 30, 50)
    door.end_fill()

    wn.exitonclick()

main()