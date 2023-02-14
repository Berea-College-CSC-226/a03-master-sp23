# Author: Veronica Agyapong
# Username1: Agyapongv
# Assignment: A03: Functional Turtles
# Purpose: Explore the use of functions with the turtle library
# Got some information from : https://www.geeksforgeeks.org/draw-house-using-turtle-programming-in-python/
import turtle

wn = turtle.Screen()  # creating and defining the variables
rays = turtle.Turtle()

house = turtle.Turtle()
s = turtle.Turtle()
sun = turtle.Turtle()
wn.colormode(1.0)
wn.bgcolor((144/255, 238/255, 144/255)) # using the RGB to create lightgreen


rays.pencolor("pink")
rays.penup()


def draw_t():  # create body of the house
    """ This function draws a house and fill it with color"""

    house.penup()
    house.speed(-10)
    house.pensize(6)

    house.color((225/225, 160/225, 0/225)) # using the RGB intensity for lightorange
    house.begin_fill()
    house.goto(-200, -150)
    house.pendown()
    house.forward(400)
    house.left(90)
    house.forward(200)
    house.left(90)
    house.forward(400)
    house.left(90)
    house.forward(200)
    house.left(90)
    house.end_fill()

    house.forward(100)  # create partition
    house.left(90)
    house.forward(200)
    house.left(90)
    house.end_fill()
    house.forward(100)

    house.color("red", "brown")  # creating the roof
    house.begin_fill()
    house.speed(-10)
    house.right(120)
    house.forward(100)
    house.right(120)
    house.forward(100)
    house.end_fill()

    house.begin_fill()  # fill the roof
    house.backward(100)
    house.left(60)
    house.forward(300)
    house.right(60)
    house.forward(100)
    house.end_fill()
    house.hideturtle()

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
    s.penup()  # using the same turtle to draw the door of the house
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
    s.goto(-202, 50)

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
    s.hideturtle()

def sun_rays():
    for i in range(2):  # creating codes for the house body
        sun.penup()
        sun.goto(00, 190)
        sun.pendown()
        sun.color("yellow")
        sun.color((224/224, 224/224, 0/224)) # using the RGB intensity of yellow
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