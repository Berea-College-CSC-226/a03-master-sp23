######################################################################
# Author: Ariadne Tynes             TODO: Change this to your name, if modifying
# Username: aritynes                     TODO: Change this to your username, if modifying#
# Assignment: A03 Fully Functional Gitty Psychedelic Robotic Turtles
# Purpose: To demonstrate the turtle library and loops
#Google doc link: https://docs.google.com/document/d/1BVPiOTm0ybNICS0PFnBczvnh2sVbBALwMW4frgE1nmw/edit?usp=sharing
######################################################################
import turtle
def function_1(jay,size):
    """
draws a square to make the base of the house
    """
    pass
    for i in range(4):
        jay.forward(size)
        jay.left(90)
    jay.penup()
    jay.pencolor("brown")
    jay.setpos(30,-40)
    jay.pendown()
    jay.begin_fill()
    jay.fillcolor("brown")
    for i in range(2):             # loop to create doors
        jay.left(90)
        jay.forward(50)
        jay.left(90)
        jay.forward(30)
    jay.end_fill()
    jay.hideturtle()

def function_2(t,size):
    """
draws the roof of house
    """
    pass
    for i in range(3):
        t.forward(size)
        t.left(120)

def function_3(t,size):
    """
function to create window 1
    :return:
    """
    for i in range(4):
        t.forward(size)
        t.left(90)

    t.penup()               #horizontal line
    t.setpos(40,75)
    t.pendown()
    t.forward(30)

    t.penup()              # vertical line
    t.setpos(55, 60)
    t.pendown()
    t.left(90)
    t.forward(30)

def function_4(t,size):
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.penup()  # horizontal line
    t.setpos(-25, 60)
    t.pendown()
    t.forward(30)

    t.penup()  # vertical line
    t.setpos(-10, 75)
    t.pendown()
    t.left(90)
    t.forward(30)
    t.hideturtle()

def Star(jay,size):               # function to draw stars
    jay.begin_fill()
    jay.fillcolor("#FFEA00")
    for i in range(5):
        jay.forward(size)
        jay.right(144)
    jay.end_fill()

def function_5(jay,size):
    jay.color("#FFEA00")  # code for different stars
    jay.penup()
    jay.setpos(-200, 230)

    for i in range(6):
        Star(jay, size)
        jay.left(45)
        jay.forward(80)


        Star(jay, size)
        jay.right(55)
        jay.forward(85)



def main():
    """


    """
    wn = turtle.Screen()                    # code to begin base of the house
    wn.bgcolor(0.9046,0.9649,0.5598)
    jay = turtle.Turtle()
    jay.pensize(3)
    jay.pencolor("dark sea green")
    jay.penup()
    jay.setpos(-60,-40)
    jay.pendown()
    function_1(jay,150)

    t = turtle.Turtle()                    # code to draw roof
    t.pensize(3)
    t.pencolor("dark green")
    t.penup()
    t.setpos(-60,110)
    t.pendown()
    t.fillcolor("dark sea green")
    t.begin_fill()
    function_2(t,150)
    t.end_fill()

    t.penup()                          # code for windows
    t.setpos(40,60)
    t.pendown()
    t.pencolor("black")
    function_3(t,30)
    t.penup()
    t.setpos(-10,60)
    t.pendown()
    function_4(t,30)

    jay.pencolor("#D3D3D3")         # code to make moon
    jay.penup()
    jay.setpos(-600,230)
    jay.pendown()
    jay.begin_fill()
    jay.fillcolor("#D3D3D3")
    jay.circle(100)
    jay.end_fill()


    function_5(jay,65)
    wn.exitonclick()

main()
