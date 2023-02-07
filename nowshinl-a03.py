# Author: Lamia Nowshin
# Username: nowshinl
#
# Assignment: A03: Functional Turtles
# repository: https://github.com/Berea-College-CSC-226/a03-master-sp23.git
# Google Doc: https://docs.google.com/document/d/1BvdBldwg6mqrr9gc2klA_hgBGR6kyxuckmeBAway7y0/edit?usp=sharing

import turtle #importing turtle and math module

def base():
    """
    starting to create the base of the house, so I need a rectangle
    """
    turtle.fillcolor("cyan")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)

    turtle.forward(250)

    turtle.left(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.end_fill()

def top_house():
    """
     creating the top of the house by drawing a triangle
    """
    turtle.fillcolor('brown')
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.left(180)
    turtle.forward(200)
    turtle.right(135)
    turtle.forward(259)
    turtle.right(90)
    turtle.forward(142)
    turtle.end_fill()

def door_window():
    """
    this function creates the door and windows
    """
    turtle.right(90) #adding door and windows
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(180)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(150)

    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(200)

def writing(write):
    write.ht()
    write.left(180)
    write.penup()
    write.forward(180)
    write.write("Turtle House!", font=[50])
def main():
    """
    the is the main function
    """
    screen = turtle.Screen()  # choosing a background color for output screen
    screen.bgcolor("#FFFF00")

    write = turtle.Turtle()
    write.ht()

    turtle.color("black")  # choosing the color and speed of turtle(pen) that will draw the house on the screen
    turtle.shape("turtle")
    turtle.speed(0)
    base() #calling the base function
    top_house() #calling the top of the house
    door_window() #calling door and windows
    writing(write) #calling the writing function

    turtle.exitonclick()

main() #calling the main function





