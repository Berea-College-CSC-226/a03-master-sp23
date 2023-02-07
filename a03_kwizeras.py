# Author: Sotaire Kwizera
# Username: kwizeras
# Google Doc: https://docs.google.com/document/d/1Dm4AIsFQXNA-qqIyLjPiEFVhvKB0Z2507Vo6T2dZet0/edit?usp=sharing

import turtle
def field():
                                               # This field create the rectangular shape of the soccer field and fill it with green


    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(-200, -200)                      # Specifying the starting position of my turtle
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    for i in range(2):                     # a for loop that builds the rectangle in 2 steps.
        t.forward(300)
        t.left(90)
        t.fd(500)
        t.left(90)
    t.end_fill()
    t.penup()
    t.right(59)
    t.fd(10)
    t.left(45)
    t.fd(400)
    t.pencolor("pink")
    t.pensize(20)
    t.write("Welcome to my Sexy soccer field!", font = ('Arial', 25, 'normal'), align= "right", move = True)    # writes down the welcome message.
    t.penup()
    t.fd(300)
r=20                                                # Specifies the ridius of my circles
def lines():
                                                    # Draws required lines in the field

    t1 = turtle.Turtle()
    t1.speed(10)
    t1.penup()
    t1.goto(-200, 70)
    t1.pendown()
    t1. fillcolor("#FEFDFC")
    t1.pencolor("#FEFDFC")
    t1.fd(300)
    t1.bk(175)
    t1.right(90)
    t1.fd(2)
    t1.circle(r)
    t1.penup()
    t1.left(90)
    t1.fd(18)
    t1.pendown()
    t1.circle(radius=r/10)                       # Draws the little center point
    t1.penup()
    t1.goto(-100, 600)
def goalies():

                                               # Draws the golies
    t2 = turtle.Turtle()
    t2.penup()
    t2.goto(-120, 300)
    t2.pendown()
    t2.speed(10)
    t2.pencolor("#FEFDFC")
    for i in range(2):                         #Draws the first little goalie rectangles
        t2.fd(140)
        t2.right(90)
        t2.fd(70)
        t2.right(90)
    t2.right(90)
    t2.penup()
    t2.fd(430)
    t2.left(90)
    t2.pendown()
    for i in range(2):                        #Draws the second little goalie rectangles
        t2.fd(140)
        t2.right(90)
        t2.fd(70)
        t2.right(90)
    t2.fd(110)
    t2.left(90)
    t2.circle(40,180)                       #Draw the first goalie semi-circle
    t2.left(180)
    t2.penup()
    t2.fd(359)
    t2.right(180)
    t2.pendown()
    t2.circle(40, 180)                      #Draw the second goalie semi-circle
    t2.penup()
    t2.fd(50)
    t2.left(90)
    t2.fd(8)
    t2.pendown()
    for i in range(2):                     # Draws the first inner goalie rectangle
        t2.fd(70)
        t2.right(90)
        t2.fd(20)
        t2.right(90)
    t2.penup()
    t2.left(90)
    t2.fd(480)
    t2.right(90)
    t2.pendown()
    for i in range(2):                     # Draws the second inner goalie rectangle
        t2.fd(70)
        t2.right(90)
        t2.fd(20)
        t2.right(90)
    t2.penup()
    t2.right(45)
    t2.fd(50)
    t2.pendown()
    t2.circle(radius=r / 10)                  # Draws the first ball circle in the goalie area
    t2.right(45)
    t2.penup()
    t2.fd(433)
    t2.pendown()
    t2.circle(radius=r / 10)                 # Draws the second ball circle in the goalie area
    t2.penup()
    t2.fd(300)

def flowers1():                                  # Draws flowers along the length of the field

    t3 = turtle.Turtle()
    t3.penup()
    t3.goto(-230, -150)
    t3.pendown()
    t3.speed(2000)
    for i in range(7):                                # Draws the same flower 7 seven times [ range (7)] on the left side of the field.
        for i in range(40):                           # create the flower
            t3.color("#F41806")
            t3.circle(19-i/2, 90)
            t3.left(90)
            t3.color("blue")
            t3.circle(19-i/2, 90)
            t3.left(18)
        t3.left(90)
        t3.penup()
        t3.fd(70)
        t3.right(90)
        t3.pendown()
    t3.right(56)
    t3.penup()
    t3.fd(610)
    t3.left(56)
    t3.fd(10)
    t3.pendown()
    for i in range(7):                                    # Draws the same flower 7 seven times [ range (7)] on the right side of the field.
        for i in range(40):                                # create the flower
            t3.color("orange")
            t3.circle(19-i/2, 90)
            t3.left(90)
            t3.color("blue")
            t3.circle(19-i/2, 90)
            t3.left(18)
        t3.left(90)
        t3.penup()
        t3.fd(70)
        t3.right(90)
        t3.pendown()



def main():                                       # The main function of the program, where all things belong

    win = turtle.Screen()                         # Creating the turtle screen
    turtle.Screen().bgcolor("#0B5345")            # Creating the turtle screen background color.
    field()
    lines()
    goalies()
    flowers1()
    win.exitonclick()

main()