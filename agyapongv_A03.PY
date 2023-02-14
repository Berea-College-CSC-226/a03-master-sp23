#Author: Veronica Agyapong
# Username1: Agyapongv
# Assignment: A03: Functional Turtles
# Purpose: Explore the use of functions with the turtle library
# Got some information from : https://www.geeksforgeeks.org/draw-house-using-turtle-programming-in-python/
import turtle
wn = turtle.Screen() #creating and defining the variables
rays = turtle.Turtle()

t = turtle.Turtle()
s = turtle.Turtle()
sun = turtle.Turtle()

wn.bgcolor("green")
rays.pencolor("pink")
rays.penup()






def draw_t(): # create body of the house
    """ This function draws a house and fill it with color"""


    t.penup()
    t.speed(-10)
    t.pensize(6)
    t.color("brown")
    t.begin_fill()
    t.goto(-200, -150)
    t.pendown()
    t.forward(400)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.end_fill()


    t.forward(100)           # create partition
    t.left(90)
    t.forward(200)
    t.left(90)
    t.end_fill()
    t.forward(100)


    t.color("red", "violet")  # creating the roof
    t.begin_fill()
    t.speed(-10)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.end_fill()


    t.begin_fill()              # fill the roof
    t.backward(100)
    t.left(60)
    t.forward(300)
    t.right(60)
    t.forward(100)
    t.end_fill()
def s_style():
    """This function draw the roof of the house"""
    s.penup()
    s.goto(202, 50)
    s.pendown()

    s.speed(-10)
    s.pendown()
    s.color("orange")
    s.left(90)
    s.pensize(3)
    s.pencolor("indigo")
    s.left(90)
    s.end_fill()

    s.forward(60)
    s.left(90)
    s.forward(60)
    s.left(90)
    s.forward(60)
    s.left(90)
    s.forward(60)
    s.penup()       # using the same turtle to draw the door of the house 
    s.goto(30, 0)
    s.pendown()
    s.left(90)
    s.speed(-10)
    s.backward(60)
    s.left(90)
    s.forward(150)
    s.backward(150)
    s.right(90)
    s.forward(70)
    s.left(90)
    s.forward(155)


    s.penup()
    s.goto(-202,50)


    s.left(90)
    s.forward(100)
    s.pendown()
    s.forward(60)
    s.right(90)
    s.forward(60)
    s.right(90)
    s.forward(60)
    s.right(90)
    s.forward(60)
    s.backward(200)
    s.penup()

def sun_rays():
    for i in range(2):  # creating codes for the house body
        sun.penup()
        sun.goto(00, 190)
        sun.pendown()
        sun.color("yellow")
        sun.fillcolor("yellow")
        sun.begin_fill()
        sun.pensize(2)
        sun.circle(40)
        sun.end_fill()
    for i in range(22):
        sun.right(90)
        sun.fd(30)
        sun.backward(30)
        sun.left(90)
        sun.circle(40, 20)




def main():

    draw_t()
    s_style()
   
    sun_rays()
if __name__ == "__main__":
    main()

wn.exitonclick()