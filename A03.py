## Lawrence Griffey, griffeyl2
# https://docs.google.com/document/d/1aZtVimL4sxi8CWJrASJqCyV5D6DIi2YWu5Mvi19Qcm4/edit?usp=sharing

import turtle
from turtle import Turtle

wn = turtle.Screen()
law = turtle.Turtle()
wn.bgcolor("blue")
maw: Turtle = turtle.Turtle()
# turtle attributes
law.speed(100)
law.pensize(3)
law.color("orchid")
maw.color("orchid")

# outline of panda head

maw.penup()
maw.setposition(-25, -10)
maw.begin_fill()
maw.circle(100)
maw.end_fill()


# first panda ear4

def panda():
    law.fillcolor("black")
    law.pencolor("black")
    law.penup()
    law.setposition(-100, 150)
    law.pendown()
    law.begin_fill()
    law.circle(30, extent=400)
    law.end_fill()

    law.penup()
    law.goto(80, 150)
    law.pendown()
    law.begin_fill()
    law.circle(30, extent=400)
    law.end_fill()
    maw.goto(20, 100)


# first eye
def eyes(radius):
    maw.color("black")
    # maw.goto(20, 100)
    maw.begin_fill()
    maw.circle(radius)
    maw.end_fill()


def nose():
    maw.goto(-25, 20)
    maw.pendown()
    maw.pencolor("black")
    maw.fillcolor("black")
    maw.begin_fill()
    maw.circle(20)
    maw.end_fill()


def main():
    panda()
    eyes(25)
    maw.goto(-60, 100)
    eyes(25)
    nose()


main()

# second eye


# white part of the eyes


# second white part of the eyes


# panda's mouth


wn.exitonclick()
