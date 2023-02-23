#################################################################################
# Author:Layla Planas
# Username: planasl
#
# Assignment: Gitty Psychedelic Robot Turtles
# Purpose: to learn turtles, functions and git hub
#################################################################################
# Google Doc Link: https://docs.google.com/document/d/1iG-ygCvsQ75cqErzChl46wvnyW72l1yXjyMgZ-q76dA/edit?usp=sharing
#
#
#################################################################################

import turtle
# Set up the turtle screen and turtle object
wn = turtle.Screen()
t = turtle.Turtle()

def house():
    # Draw the house body
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.end_fill()

    # Draw the roof
    t.penup()
    t.goto(-100,100)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.left(45)
    t.forward(140)
    t.right(90)
    t.forward(140)
    t.end_fill()

    # Draw the door
    t.penup()
    t.goto(0,-100)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.end_fill()

    # Draw the windows
    t.penup()
    t.goto(-70,0)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.end_fill()

    t.penup()
    t.goto(70,0)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.end_fill()


house()
# Hide the turtle object and exit the turtle screen
t.hideturtle()
wn.exitonclick()