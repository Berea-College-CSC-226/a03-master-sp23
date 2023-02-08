#################################################################################
# Author:Trinity Lewis
# Username: tr1n1tyjade
#
# Assignment: A03: Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: learning more about functions and turtles
#################################################################################
# Google Doc Link: https://docs.google.com/document/d/1_xeR8gYxdERXUIvQFbpaiYTYMtlk-4gmxeqQvA-EvA4/edit?usp=sharing
# Github Repo: https://github.com/tr1n1tyjade/a03-master-sp23
#
#################################################################################

import turtle

turtle.colormode(255)

wn = turtle.Screen()
wn.setup(612, 339)
wn.bgpic("istockphoto-1337288211-612x612.gif")

def laptop():
    # this sets the top half of the laptop
    top = turtle.Turtle()
    top.penup()
    top.goto(-125, -75)

    top.pendown()
    top.pencolor(93, 135, 164)
    top.pensize(5)

    for i in range(2):
        # this will make top part of laptop
        top.begin_fill()
        top.fillcolor(93, 135, 164)
        top.forward(250)  # Moving the turtle Forward by 140 units
        top.left(90)
        top.forward(125)
        top.left(90)
        top.end_fill()
        top.hideturtle()

def screen():
    # black screen of laptop
    scrn = turtle.Turtle()
    scrn.penup()
    scrn.goto(-100, -60)

    scrn.pendown()
    scrn.pencolor(0, 0, 0)
    scrn.pensize(5)

    for i in range(2):
        scrn.begin_fill()
        scrn.fillcolor(0, 0, 0)
        scrn.forward(200)  # Moving the turtle Forward by 140 units
        scrn.left(90)
        scrn.forward(100)
        scrn.left(90)
        scrn.end_fill()
        scrn.hideturtle()

def bottom():
    # this will make bottom part of laptop
    bot = turtle.Turtle()
    bot.penup()
    bot.goto(-125, -75)

    bot.pendown()
    bot.pencolor(56, 85, 105)
    bot.pensize(5)

    for i in range(1):

        bot.begin_fill()
        bot.fillcolor(56, 85, 105)
        bot.forward(250)  # Moving the turtle Forward by 140 units
        bot.left(300)
        bot.forward(50)
        bot.left(-120)
        bot.forward(300)
        bot.left(-120)
        bot.forward(50)
        bot.end_fill()
        bot.penup()

def cord():
    line = turtle.Turtle()
    line.pencolor(220,220,220)
    line.pensize(1)
    line.penup()
    line.goto(130, -75)
    line.pendown()


    length = 5
    angle = 45
    line.forward(length)
    line.right(angle)
    line.forward(length)
    line.left(angle)
    line.forward(length)
    line.right(angle)
    line.forward(length)
    line.left(angle)
    line.forward(length)
    line.right(angle)
    line.forward(length)
    line.right(angle)
    line.forward(length)
    line.left(angle)
    line.forward(length)
    line.forward(length)
    line.right(angle)
    line.forward(length)
    line.left(angle)
    line.forward(length)
    line.right(angle)
    line.forward(length)
    line.left(angle)
    line.forward(length)
    line.right(angle)
    line.forward(length)
    line.right(angle)
    line.forward(length)
    line.left(angle)
    line.forward(length)
    line.left(10)
    line.hideturtle()


def mouse():
    m = turtle.Turtle()
    m.penup()
    m.goto(175,-140)
    m.pendown()

    m.color(0, 0, 0)
    m.begin_fill()
    m.fillcolor(0, 0, 0)
    m.circle(20)
    m.end_fill()
    m.hideturtle()

    m.penup()
    m.goto(190,-105)
    m.pendown()

    m.color(105,105,105)
    m.left(90)
    m.begin_fill()
    m.fillcolor(105, 105, 105)
    m.left(45)
    m.circle(20,180)
    m.end_fill()
    m.hideturtle()

    m.penup()
    m.goto(176,-118)
    m.pendown()

    m.color(0, 0, 0)
    m.left(190)
    m.forward(20)

def munky():
    wn.addshape("ezgif.com-gif-maker.gif")
    monke = turtle.Turtle()
    monke.left(-90)
    monke.forward(10)
    monke.shape("ezgif.com-gif-maker.gif")

def main():
    laptop()
    screen()
    bottom()
    cord()
    mouse()
    munky()

main()

wn.exitonclick()
