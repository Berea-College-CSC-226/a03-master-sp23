################################################################################
# Name: Nick Lewand
# Username: lewandn
# Repo link: https://github.com/Berea-College-CSC-226/a03-master-sp23.git
# Google Doc link: https://docs.google.com/document/d/17-xZx4gKxhlT2_8qPZ647krFdcomP5ySS_NfVP8qqI4/edit#
########################################################################################
import turtle
wn = turtle.Screen()            # general setup stuff
chonk = turtle.Turtle()
chonk.speed(10)
chonk.pensize(10)
wn.colormode(255)
wn.bgcolor(0,213,255)

def cloud():                    # first cloud
    for i in range (1):
        chonk.penup()
        chonk.goto(-250,-50)
        chonk.pendown()
        chonk.pencolor("white")
        chonk.fillcolor("white")
        chonk.begin_fill()
        chonk.circle(75,-200)
        chonk.left(90)
        chonk.circle(75,-140)
        chonk.left(90)
        chonk.circle(75,-200)
        chonk.back(200)
        chonk.end_fill()

def cloud2():                   # second cloud
    for i in range (2):
        chonk.penup()
        chonk.goto(150, -215)
        chonk.pendown()
        chonk.pencolor("white")
        chonk.fillcolor("white")
        chonk.begin_fill()
        chonk.circle(75, -200)
        chonk.left(90)
        chonk.circle(75, -140)
        chonk.left(90)
        chonk.circle(75, -200)
        chonk.back(200)
        chonk.end_fill()

def sun():                  # making the sun
    for i in range(3):
        chonk.penup()
        chonk.goto(400,300)
        chonk.pendown()
        chonk.pencolor("yellow")
        chonk.fillcolor("yellow")
        chonk.begin_fill()
        chonk.circle(100,360)
        chonk.end_fill()

def main():
    wn.exitonclick()

cloud()
cloud2()
sun()
main()
