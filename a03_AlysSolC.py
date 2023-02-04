######################################################################
# Author: Alys Combs
# Username: AlysSolC
# Assignment: A03
######################################################################
#imports..
import turtle
import random

def turtStartPoint(turt, x, y):
    """A shortcut for telling turtles where they need to go"""
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
def setup():
    """Creates window & assigns attributes for it. Also defines multiple turtles and assigns attributes to each of them."""
    wn = turtle.Screen()
    wn.bgcolor("#29BDF3")
    #grass turtle
    global gTurt
    gTurt = turtle.Turtle()
    turtStartPoint(gTurt,-400, -100)
    gTurt.color("#0EB730")
    #tree bark turtle
    global bTurt
    bTurt = turtle.Turtle()
    turtStartPoint(bTurt,-10,-100)
    bTurt.color("#AB6604")
    #leaf turtle 1
    global l1Turt
    l1Turt = turtle.Turtle()
    turtStartPoint(l1Turt, -30, 160)
    l1Turt.color("#0C6D01")
    # leaf turtle 2
    global l2Turt
    l2Turt = turtle.Turtle()
    turtStartPoint(l2Turt, 40, 190)
    l2Turt.color("#1CA90B")
    #leaf turtle 3
    global l3Turt
    l3Turt = turtle.Turtle()
    turtStartPoint(l3Turt, 50, 180)
    l3Turt.color("#0C6D01")

def branch(turt, treeside, length):
    """Meant to be used in the bark function, shortcut for drawing tree branches"""
    if treeside == "left":
        turt.left(30)
        turt.forward(length)
        turt.right(90)
        turt.forward(10)
        turt.right(90)
        turt.forward(length)
        turt.left(150)
    elif treeside == "right":
        turt.left(150)
        turt.forward(length)
        turt.right(90)
        turt.forward(10)
        turt.right(90)
        turt.forward(length)
        turt.left(30)
def bark(turt):
    """draws all of the wood of a tree"""
    turt.left(90)
    turt.forward(150)
    branch(turt, "left", 60)
    turt.forward(90)
    turt.right(90)
    turt.forward(60)
    turt.right(90)
    turt.forward(60)
    branch(turt, "right", 80)
    turt.forward(30)
    branch(turt, "right", 50)
    turt.forward(145)
    turt.right(90)
    turt.forward(90)

def leaves(turt, size):
    """Uses a specific turtle to draw leaves of a custom size."""
    turt.speed(0)
    for i in range(40):
        randnum = random.randint(1,10)
        turt.circle(size * 4)
        turt.right(size * randnum)
        turt.forward(size)

def tree():
    """Puts together all the elements of our tree"""
    bTurt.begin_fill()
    bark(bTurt)
    bTurt.end_fill()
    bTurt.right(120)
    bTurt.forward(10)
    leaves(l1Turt, 10)
    leaves(l2Turt, 10)
    leaves(l1Turt, 6)
    leaves(l2Turt,5)
    leaves(l3Turt, 7)

def grass(turt):
    """Draws the outline of some grass and fills it in."""
    turt.left(60)
    turt.speed(0)
    gX = int(gTurt.xcor())
    turt.begin_fill()
    while gX < 400:
        turt.forward(10)
        turt.right(120)
        turt.forward(10)
        turt.left(120)
        gX = int(gTurt.xcor())
    turt.right(150)
    turt.forward(200)
    turt.right(90)
    turt.goto(-400, -300)
    turt.goto(-400, -100)
    turt.end_fill()

def main():
    setup()
    tree()
    grass(gTurt)
    turtle.exitonclick()

main()
