#Author: Veronica Agyapong
# Username1: Agyapongv
# Assignment: A03: Functional Turtles
# Purpose: Explore the use of functions with the turtle library

import turtle
wn = turtle.Screen() #creating and defining the variables
love = turtle.Turtle()
house = turtle.Turtle()
t = turtle.Turtle()
s = turtle.Turtle()
sr = turtle.Turtle()
wn.bgcolor("green")
love.pencolor("pink")
love.penup()
love.goto(-0, -250)






def draw_t(): # create body of the house
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


    t.forward(100)# create partition
    t.left(90)
    t.forward(200)
    t.left(90)
    t.end_fill()
    t.forward(100)


    t.color("red", "violet")# creating the roof
    t.begin_fill()
    t.speed(-10)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.end_fill()


    t.begin_fill()# fill the roof
    t.backward(100)
    t.left(60)
    t.forward(300)
    t.right(60)
    t.forward(100)
    t.end_fill()
def s_style():
    s.penup()
    s.goto(202, 50)
    s.speed(-10)
    s.pendown()
    s.color("orange")
    s.left(90)
    s.pensize(3)
    s.pencolor("indigo")
    s.left(90)

    s.forward(60)
    s.left(90)
    s.forward(60)
    s.left(90)
    s.forward(60)
    s.left(90)
    s.forward(60)
    s.penup() #  the door
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
def love_vals():
    for i in range(2):  # creating codes for the circle sun shape
        love.penup()
        love.goto(00, 170)
        love.pendown()
        love.color("yellow")
        love.fillcolor("yellow")
        love.begin_fill()
        love.pensize(2)
        love.circle(30)
        love.end_fill()
        love.penup()
def sun_rays():
    for i in range(12):
        love.penup()
        love.goto(0,200)
        love.pendown()
        love.right(360/ 12 * i )
        love.forward(50)
        love.backward(100)
        love.right(90)
        love.penup()
        love.goto(-130,270)
        love.write("IT IS VERY SUNNY TODAY", font=("Times New Roman",16,"normal"))

                            #Create the turtle object


def main():

    draw_t()
    s_style()
    love_vals()
    sun_rays()
if __name__ == "__main__":
    main()

wn.exitonclick()