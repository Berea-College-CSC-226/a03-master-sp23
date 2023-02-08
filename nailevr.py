######################################################################
# Author: Rinat Nailev
# Username: nailevr
#
# Assignment: A03:

######################################################################
# Acknowledgements:
# Original: http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
#
# Dr. Jan Pearce - this file is modified from her original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle
import random
yo = turtle.Turtle()





def randomizing(number_of_stars, size, color):  #making starts appear in random spots

    for e in range(number_of_stars):
        yo.penup()
        yo.goto(random.randrange(-300, 300), random.randrange(-100, 300))
        yo.pendown()
        star(size, color)

def star(size, color): #draw a star
    yo.color(color)
    yo.begin_fill()
    for i in range(5):
        yo.forward(size)
        yo.right(144)
    yo.end_fill()

def person1(personsize): #draw person1
    yo.penup()
    yo.color("white")
    yo.pensize(10)
    yo.goto(0, -300)
    yo.left(90)
    yo.pendown()
    yo.begin_fill()
    yo.forward(personsize)
    yo.right(90)
    yo.circle(personsize/4)
    yo.end_fill()
    yo.penup()
    yo.goto(0, personsize/2-300)
    yo.pendown()
    yo.left(40)
    yo.forward(personsize/3)
    yo.left(20)
    yo.forward(personsize/4)

def person2(personsize): #draw person2
    yo.penup()
    yo.color("white")
    yo.pensize(10)
    yo.goto(-70, -300)
    yo.left(30)
    yo.pendown()
    yo.begin_fill()
    yo.forward(personsize)
    yo.right(90)
    yo.circle(personsize/4)
    yo.end_fill()

def text(): #write a text
    yo.penup()
    yo.goto(200,-200)
    yo.write("Late Night Date", font=("Verdana", 15, "normal"))
    yo.pendown()





def main(): #important

    wn = turtle.Screen()
    wn.colormode(255)
    wn.screensize(600)
    wn.bgcolor(19, 24, 98)

    yo.speed(0)
    number_of_stars = int(input("How many starts would you like?\n"))
    randomizing(number_of_stars, 15, "yellow")
    person1(100)
    person2(100)
    text()
    wn.exitonclick()


main()







