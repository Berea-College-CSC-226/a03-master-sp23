#Author: Liliane Azabe
# Username1: azabel
# Assignment: A03: Functional Turtles
# Purpose: Explore the use of functions with the turtle library

#some information adapted from https://realpython.com/beginners-guide-python-turtle/
#################################################################################

import turtle
import math
wn = turtle.Screen()
wn.bgcolor("#964B00")
wn.title(" Liliane's Dream House")
alex = turtle.Turtle()
alex.color("#738B7A")
alex.speed(6)

lily = turtle.Turtle()
lily.color("#00FA00")
lily.speed(6)
#
toy = turtle.Turtle()
toy.pensize(3)
toy.color("#A020F0")
def draw_house_body():            #drawing the lower body of the house
    """
    this function draws the lower body of the house
    :return: no return(it's a non-fruitful function)
    """
    toy.begin_fill()
    toy.forward(400)
    toy.left(90)
    toy.forward(200)
    toy.left(90)
    toy.end_fill()
def create_parts():         # creating some house parts..LIKE SIDES  OF THE HOUSE
    """
    this function creates the side parts of the house
    :return: no return; it's a non_fruitful function
    """
    toy.forward(100)
    toy.left(90)
    toy.forward(200)
    toy.left(90)
    toy.forward(100)

def create_window():         #CREATING WINDOW OF THE HOUSE
    """
    this function creates the window of the house
    :return: no return because it's a non_fruitful function
    """
    lily.goto(-40,-50)
    lily.pendown()
    lily.color("#000000","#FD6BBE")
    lily.begin_fill()
    lily.backward(50)
    lily.left(90)
    lily.forward(60)
    lily.right(90)
    lily.forward(50)
    lily.right(90)
    lily.forward(60)
    lily.right(90)
    lily.forward(25)
    lily.right(90)
    lily.forward(60)
    lily.backward(60)
    lily.right(90)
    lily.forward(25)
    lily.backward(50)
    lily.end_fill()

def create_roof():                       #CREATING THE ROOF OF THE HOUSE
    """
    This function creates a roof for the house
    :return: N/A since it's a non_fruitful function
    """
    toy.color("#000000", "#8B0000")
    toy.begin_fill()
    toy.right(120)
    toy.forward(100)
    toy.right(120)
    toy.forward(100)
    toy.end_fill()
    toy.begin_fill()
    toy.backward(100)
    toy.left(60)
    toy.forward(300)
    toy.right(60)
    toy.forward(100)
    toy.end_fill()


def create_door():                  #Creating our little door
    """
    this function helps create the door of the house
    :return: N/A since this is the non_fruitful function
    """
    toy.penup()
    toy.goto(-200,-150)
    toy.setheading(0)
    toy.pendown()
    toy.color("#A020F0","#800000")
    toy.forward(230)
    toy.left(90)
    toy.begin_fill()
    toy.forward(90)
    toy.right(90)
    toy.forward(50)
    toy.right(90)
    toy.forward(90)
    toy.end_fill()
    toy.penup()

def create_sunshine():                #Creating the sun for the house
    """
    this function helps to create the sun
    :return: N/A: it's a non_fruitful function
    """
    alex.penup()
    alex.goto(-350,150)
    alex.pendown()
    alex.color("#FFD343", "#FFD343")
    alex.begin_fill()
    alex.circle(45)
    alex.end_fill()
def draw_rays():          #creating the sun rays
    """
    this function helps draw the sun rays on the sun
    :return: N/A since this is a non_fruitful function
    """
    alex.pensize(6)
    alex.forward(80)
    alex.backward(80)
    alex.left(30)
    alex.end_fill()
def create_clouds():    # creating the clouds for climate showoff!!
    """
    this function creates the clouds next to the house
    :return: N/A since this is a non_fruitful function
    """
    lily.penup()
    lily.goto(360, 200)
    lily.pendown()
    lily.color("sky blue", "sky blue")
    lily.setheading(90)
    lily.begin_fill()
    lily.circle(40, 180)
    lily.end_fill()
    lily.goto(400, 200)
    lily.setheading(90)
    lily.begin_fill()
    lily.circle(80, 180)
    lily.end_fill()
def create_rain():              # created the clouds that produces rain!!
    """
    this function creates the rain to rain from the clouds
    :return: N/A since this is a non_fruitful function
    """
    for i in range(15):
        lily.penup()
        lily.stamp()
        lily.shape("classic")
        lily.forward(30)


def draw_this():                # making turtle write for the little warm welcome to the house
    """
    This function draws the text over the house
    :return: N/A since this is a non_fruitful function
    """
    lily.penup()
    lily.pensize(10)
    lily.color()
    lily.goto(-160,200)
    lily.pendown()
    lily.write("WELCOME TO \n MY HOUSE", font=("Areal", 40, "bold"))




def main():               # this is where the function were called!
    """
    this function helps to get most of other functions executed and get the whole house, rain and sun together
    :return: N/A since this is a non_fruitful function
    """
    toy.penup()
    toy.begin_fill()
    toy.fillcolor("#030303")
    toy.goto(-200, -150)
    toy.pendown()
    for i in range(2):
        draw_house_body()
    toy.end_fill()
    create_parts()
    create_window()
    create_roof()
    create_door()
    create_sunshine()
    alex.goto(-350, 190)
    alex.pendown()
    for i in range(12):
        draw_rays()
    alex.penup()
    draw_this()
    create_clouds()
    lily.goto(365, 200)
    create_rain()
    lily.goto(345, 200)
    create_rain()
    lily.goto(320, 200)
    create_rain()
    lily.goto(300, 200)
    create_rain()
    lily.goto(280, 200)
    create_rain()
    lily.goto(260, 200)
    create_rain()


main()

wn.exitonclick()



