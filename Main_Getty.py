import turtle
wn = turtle.Screen()
wn.bgcolor("green")


# Create new Turtle
my_turtle = turtle.Turtle()

# Build the house
my_turtle.penup()
my_turtle.goto(-200, 0)
my_turtle.pendown()
my_turtle.color("#FF0000")
my_turtle.fillcolor("#FF0000")
my_turtle.begin_fill()
my_turtle.forward(200)
my_turtle.left(90)
my_turtle.forward(200)
my_turtle.left(90)
my_turtle.forward(200)
my_turtle.left(90)
my_turtle.forward(200)
my_turtle.end_fill()

# Build the roof
my_turtle.penup()
my_turtle.goto(0, 200)
my_turtle.pendown()
my_turtle.color("#FF0000")
my_turtle.fillcolor("#FF0000")
my_turtle.begin_fill()
my_turtle.left(45)
my_turtle.forward(141.4)
my_turtle.right(90)
my_turtle.forward(141.4)
my_turtle.end_fill()

# Build the door
my_turtle.penup()
my_turtle.goto(-75, 0)
my_turtle.pendown()
my_turtle.color("#FFFF00")
my_turtle.fillcolor("#FFFF00")
my_turtle.begin_fill()
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(150)
my_turtle.end_fill()

# Build the windows
my_turtle.penup()
my_turtle.goto(-125, 100)
my_turtle.pendown()
my_turtle.color("#0000FF")
my_turtle.fillcolor("#0000FF")
my_turtle.begin_fill()
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(25, 100)
my_turtle.pendown()
my_turtle.color("#0000FF")
my_turtle.fillcolor("#0000FF")
my_turtle.begin_fill()
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.end_fill()

# Hide the turtle
my_turtle.hideturtle()

# Keep window open
turtle.done()

