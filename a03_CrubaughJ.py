# HEADER

# David Crubaugh's Fox Drawing (CrubaughJ)
# Google Doc: https://docs.google.com/document/d/1Ge_fdmXzmHLe7J_Es64Gu3SUcqonJlOVE1zQhTHO1jQ/edit?usp=sharing

# ----------------------------------------------------------------------------------------------------------------------
# The first thing I did was to import turtle and to create the Screen and turtle (I also set the color of both)
# ----------------------------------------------------------------------------------------------------------------------

import turtle

wn = turtle.Screen()
wn.bgcolor('#000000')
fox = turtle.Turtle()
fox.color('#FFA500')


# ----------------------------------------------------------------------------------------------------------------------
# fill(x, y, c) fills the shape I found that I reused this code 3x, so I made a function for it.
# ----------------------------------------------------------------------------------------------------------------------


def fill(x, y, c):
    fox.fillcolor(c)
    fox.penup()
    fox.goto(x, y)
    fox.begin_fill()
    fox.pendown()


# ----------------------------------------------------------------------------------------------------------------------
# This was the first function I created it creates an equilateral triangle and calls the function to fill the triangle.
# ----------------------------------------------------------------------------------------------------------------------


def eq_tri(x, y, s, a, c):
    fill(x, y, c)
    for i in range(0, 3):
        fox.forward(s)
        fox.right(a)
    fox.end_fill()


# ----------------------------------------------------------------------------------------------------------------------
# This was the second function I created which makes the eyes of the fox by creating a circle.
# ----------------------------------------------------------------------------------------------------------------------


def cir(x, y, d, c):
    fill(x, y, c)
    for i in range(1):
        fox.circle(d)
        fox.end_fill()


# ----------------------------------------------------------------------------------------------------------------------
# As the name implies this gets ride of the turtle.
# ----------------------------------------------------------------------------------------------------------------------


def get_ride_of_fox():
    fox.penup()
    fox.goto(300, 300)
    fox.color('#000000')


# ----------------------------------------------------------------------------------------------------------------------
# This is where I plug in the colors and the placement of the different functions as well as there size.
# ----------------------------------------------------------------------------------------------------------------------


def main():
    eq_tri(-75, 0, 150, 120, '#FFA500')
    eq_tri(-75, 0, 40, -120, '#FFA500')
    eq_tri(-70, 0, 30, -120, '#FFFFFF')
    eq_tri(35, 0, 40, -120, '#FFA500')
    eq_tri(40, 0, 30, -120, '#FFFFFF')
    eq_tri(-20, -95, 40, 120, '#FFFFFF')

    cir(-20, -30, 5, '#000000')
    cir(20, -30, 5, '#000000')

    get_ride_of_fox()

    wn.exitonclick()


# ----------------------------------------------------------------------------------------------------------------------
# I call main.
# ----------------------------------------------------------------------------------------------------------------------


main()