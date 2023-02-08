#################################################################################
# Author:Jacob Wells
# Username:Wellsj2/TimeMender
#
# Assignment: Gitty Psychedelic Robot Turtles
# Purpose: to learn turtles, functions and git hub
#################################################################################
# Google Doc Link: https://docs.google.com/document/d/1x9SnoQbESeqN9ysqQ-fPoC7a7sJo700i0_wdFzmgj6c/edit?usp=sharing
#
#
#################################################################################
import turtle


def tortise_draws():
    """This turtle draws a moon onto the background"""
    tortise = turtle.Turtle()
    tortise.speed(9)
    tortise.pencolor("white")
    tortise.penup()
    tortise.setpos(260, 250) #Open the window to full screen to see the full piece
    tortise.pendown()
    tortise.fillcolor("white")
    tortise.begin_fill()
    tortise.circle(50)
    tortise.end_fill()
    tortise.hideturtle()


def ground():
    """This turtle draws a grassy field to pitch tents on"""
    grass = turtle.Turtle()
    grass.speed(9)
    grass.penup()
    grass.pencolor("#28AA32")
    grass.setpos(-690, 0)
    grass.fillcolor("#28AA32")
    grass.pendown()
    grass.begin_fill()
    for i in range(2):
        grass.fd(1400)
        grass.right(90)
        grass.fd(450)
        grass.right(90)
    grass.end_fill()
    grass.hideturtle()

def tent():
    """This turtle draws the first red tent onto the grassy field"""
    tenny = turtle.Turtle()
    tenny.speed(10)
    tenny.pencolor("#961E32")
    tenny.fillcolor("#961E32")
    tenny.begin_fill()
    tenny.forward(100)
    tenny.left(120)
    tenny.fd(100)
    tenny.left(120)
    tenny.fd(100)
    tenny.end_fill()
    tenny.hideturtle()

def blue_tent():
    """This turtle draws a second blue tent to join the first red tent"""
    tennty = turtle.Turtle()
    tennty.speed(10)
    tennty.setpos(120, 0)
    tennty.pencolor("#321E96")
    tennty.fillcolor("#321E96")
    tennty.begin_fill()
    tennty.forward(100)
    tennty.left(120)
    tennty.fd(100)
    tennty.left(120)
    tennty.fd(100)
    tennty.end_fill()
    tennty.hideturtle()

def green_tent():
    """This turtle draws a third and final green tent onto the grassy field"""
    trennty = turtle.Turtle()
    trennty.speed(10)
    trennty.setpos(-220, 0)
    trennty.pencolor("#509614")
    trennty.fillcolor("#509614")
    trennty.begin_fill()
    trennty.forward(100)
    trennty.left(120)
    trennty.fd(100)
    trennty.left(120)
    trennty.fd(100)
    trennty.end_fill()
    trennty.hideturtle()

def fire_pit():
    """This turtle draws a fire pit base onto the grassy field"""
    fires = turtle.Turtle()
    fires.speed(10)
    fires.penup()
    fires.setpos(-80, -20)
    fires.pencolor("#646464")
    fires.fillcolor("#646464")
    fires.pendown()
    fires.begin_fill()
    fires.forward(50)
    fires.left(90)
    fires.fd(50)
    fires.left(90)
    fires.fd(50)
    fires.left(90)
    fires.fd(50)
    fires.end_fill()
    fires.hideturtle()

def fire():
    """This final turtle draws a fire on top of the fire pit base"""
    fire = turtle.Turtle()
    fire.speed(10)
    fire.penup()
    fire.setpos(-65, 30)
    fire.pencolor("#C85A0A")
    fire.fillcolor("#C85A0A")
    fire.pendown()
    fire.begin_fill()
    fire.forward(20)
    fire.left(120)
    fire.fd(20)
    fire.left(120)
    fire.fd(20)
    fire.end_fill()
    fire.hideturtle()
def main():
    """This function runs all of the other functions"""
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("A Full Moon Night")
    tortise_draws()
    ground()
    tent()
    blue_tent()
    green_tent()
    fire_pit()
    fire()
    window.exitonclick()

main()