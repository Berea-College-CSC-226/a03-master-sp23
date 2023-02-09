# Moustapha Ndiaye
# Ndiayem
# https://docs.google.com/document/d/1TvKTq21dxkEyqbjGJvurHCt17N3w86O7WtttUl9x9so/edit?usp=sharing

import turtle

def field():
    turtle.Turtle()
    turtle.pencolor("white")
    khadija = turtle.Screen()
    khadija.bgcolor("green")
    turtle.pen(0)
    turtle.setup(124, 700)
    turtle.pensize(6)

    turtle.penup()
    turtle.goto(450, -250)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(500)
    turtle.setheading(180)
    turtle.forward(900)
    turtle.setheading(270)
    turtle.forward(500)
    turtle.setheading(0)
    turtle.forward(900)

    # Draw the right side
    turtle.goto(450, -100)
    turtle.setheading(180)
    turtle.forward(100)
    turtle.setheading(90)
    turtle.forward(200)
    turtle.setheading(0)
    turtle.forward(100)

    # Draw left side
    turtle.penup()
    turtle.goto(-450, -100)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(100)
    turtle.setheading(90)
    turtle.forward(200)
    turtle.setheading(180)
    turtle.forward(100)

    # Draw the middle line
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(500)

    # Draw the circle in the middle
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.goto(-20, -300)
    turtle.pendown()
    turtle.write("KhadiJa's Stadium")


def main():
    field()
    turtle.hideturtle()
    turtle.done()

main()

