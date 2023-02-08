#My project is an empty room that depicts the underlying desires of troubled people: safe spaces.
import turtle

#Determines the borders and size of the canvas.
def SquareDefinition(wn, alex):
    wn = turtle.Screen()
    alex.penup()
    alex.speed(5)
    alex.setpos(-180, -130)
    alex.pendown()
    alex.fillcolor(168, 169, 173)    #Sets a custom color on the RGB scale
    alex.begin_fill()
    for i in range (2):
        alex.forward(360)
        alex.left(90)
        alex.forward(260)
        alex.left(90)
    alex.end_fill()
def OuterBorder(alex):
    alex.fillcolor(150, 111, 51)
    alex.begin_fill()
    alex.right(135)
    alex.forward(200)
    print(alex.pos())       #Returns the position of the turtle
    alex.setpos(321.42, -271.42)
    alex.right(90)
    alex.forward(200)   #Completes the first corner of the outer border
    alex.end_fill()     #Fills the first corner of the outer border.

    #Starts 2nd fill and corner of outer border
    alex.fillcolor(168, 169, 173)
    alex.begin_fill()
    alex.penup()
    alex.setpos(321.42, 271.42)
    alex.pendown()
    alex.setpos(-321.42, 271.42)
    alex.setpos(-180, 130)
    alex.right(135)
    alex.forward(360)
    alex.left(45)
    alex.forward(200)
    alex.end_fill()
    #Stops 2nd fill and corner of outer border

    #Starts 3rd fill and corner
    alex.begin_fill()
    alex.right(135)
    alex.forward(543)
    alex.right(135)
    alex.forward(200)
    alex.right(45)
    alex.forward(260)
    alex.right(45)
    alex.forward(200)
    alex.end_fill()
    #Ends 3rd fill and corner

    #Starts 4th fill and corner
    alex.begin_fill()
    alex.setpos(-321.42, 271.42)
    alex.setpos(-180, 130)
    alex.setpos(-180, -130)
    alex.forward(-200)
    alex.setpos(-321.42, 271.42)
    alex.end_fill()
    #Ends 4th fill and corner

    #Reinforces the outline at the bottom.
    alex.penup()
    alex.setpos(-180, -130)
    alex.pendown()
    alex.setpos(180, -130)

def Outdoor(alex):
    #Creates the outdoor look
    alex.left(-90)
    alex.forward(50)

    alex.fillcolor(135, 206, 235)
    alex.begin_fill()
    alex.left(135)
    alex.forward(200)
    alex.right(45)
    alex.forward(110)
    alex.right(135)
    alex.forward(355)
    alex.end_fill()

    alex.right(135)
    alex.forward(110)
    alex.right(45)
    print(alex.pos())

def door(alex):
    #Creates the door in the building.
    alex.fillcolor(150,75,0)
    alex.begin_fill()
    for i in range(2):
        alex.forward(200)
        alex.right(90)
        alex.forward(70)
        alex.right(90)
    alex.end_fill()

    #Creates the doorknob
    alex.color(212, 175, 55)
    alex.penup()
    alex.shape("circle")
    alex.shapesize(0.5)
    alex.setpos(280, -64.79)
    alex.stamp()


def text(alex):
    alex.color("white")
    alex.setpos(0, 280)
    alex.write("A safe space.", move=False, align='center', font=("Arial", 25, ("bold", "normal")))

def main():
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.colormode(255)
    alex = turtle.Turtle()
    SquareDefinition(wn, alex)
    OuterBorder(alex)
    Outdoor(alex)
    door(alex)
    text(alex)
    wn.exitonclick()

main()













