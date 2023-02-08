################################################################################
# Name: Zaki Ayoubi
# Username: Ayoubim
# Repo link: https://github.com/Berea-College-CSC-226/a03-master-sp23.git
# Google Doc link: https://docs.google.com/document/d/1jfH5x7QutJ6QJgSUxd8SjumJCcupkgFu8Ujy9zlvfpw/edit#
########################################################################################

import turtle

def drawsquare (zaki, size):
    """" I defined function drawsquare to get turtle "zaki" to draw a square with "size" size"""
    for i in range(4):
        zaki.forward(size)
        zaki.left(90)


def main ():
    """I used the main function to define some attributes and invoke drawsquare function."""
    wn = turtle.Screen()
    wn.bgcolor("gray")
    zaki = turtle.Turtle()
    zaki.hideturtle()
    zaki.speed(0)
    zaki.penup()
    zaki.setpos(-220, 100)
    zaki.pendown()

    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("white")
        else:
            zaki.fillcolor(0.451, 0.5255, 0.4706)
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()


    zaki.penup()
    zaki.setpos(-220, 40)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor(0.451, 0.5255, 0.4706)
        else:
            zaki.fillcolor("white")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -20)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("white")
        else:
            zaki.fillcolor(0.451, 0.5255, 0.4706)
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -80)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor(0.451, 0.5255, 0.4706)
        else:
            zaki.fillcolor("white")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -140)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("white")
        else:
            zaki.fillcolor(0.451, 0.5255, 0.4706)
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -200)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor(0.451, 0.5255, 0.4706)
        else:
            zaki.fillcolor("white")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -260)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("white")
        else:
            zaki.fillcolor(0.451, 0.5255, 0.4706)
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -320)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor(0.451, 0.5255, 0.4706)
        else:
            zaki.fillcolor("white")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()
    wn.exitonclick()

main()

