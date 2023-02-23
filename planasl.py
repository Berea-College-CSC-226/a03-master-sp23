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
# Set up the turtle screen and turtle objects
wn = turtle.Screen()
wn.bgcolor("lightpink")

t = turtle.Turtle()
r = turtle.Turtle()
d = turtle.Turtle()
w_one = turtle.Turtle()
w_two = turtle.Turtle()

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
    r.penup()
    r.goto(-100,100)
    r.pendown()
    r.color("brown")
    r.begin_fill()
    r.left(45)
    r.forward(140)
    r.right(90)
    r.forward(140)
    r.end_fill()

    # Draw the door
    d.penup()
    d.goto(0,-100)
    d.pendown()
    d.color("yellow")
    d.begin_fill()
    d.forward(40)
    d.left(90)
    d.forward(80)
    d.left(90)
    d.forward(40)
    d.left(90)
    d.forward(80)
    d.end_fill()

    # Draw the windows
    w_one.penup()
    w_one.goto(-70,0)
    w_one.pendown()
    w_one.color("blue")
    w_one.begin_fill()
    w_one.forward(40)
    w_one.left(90)
    w_one.forward(40)
    w_one.left(90)
    w_one.forward(40)
    w_one.left(90)
    w_one.forward(40)
    w_one.end_fill()

    w_two.penup()
    w_two.goto(70,0)
    w_two.pendown()
    w_two.color("blue")
    w_two.begin_fill()
    w_two.forward(40)
    w_two.left(90)
    w_two.forward(40)
    w_two.left(90)
    w_two.forward(40)
    w_two.left(90)
    w_two.forward(40)
    w_two.end_fill()


house()
# Hide the turtles and exit the screen
t.hideturtle()
r.hideturtle()
d.hideturtle()
w_one.hideturtle()
w_two.hideturtle()

wn.exitonclick()