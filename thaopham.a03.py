######################################################################
# Author: Thao Pham
# Username: phamt2
# Date created: 02/06/2023
# Last modified: 02/07/2023

# Assignment: A03 - Functional Turtle
# Google Doc link: https://docs.google.com/document/d/12MtJEEGqLk5QCX9sYvYfRMU8EwAZ3ZPCU43SbfCn-nU/edit?usp=sharing
######################################################################

# import turtle function

import turtle

# create a new function to draw two flags
def rectangle (t, sz, sx):
    for i in range(2):
        t.forward(sz)
        t.left(90)
        t.forward(sx)
        t.left(90)

# create a new function to draw a star in my country flag
def drawStar (t, size):
    for i in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.right(144)

turtle.colormode(255)
wn = turtle.Screen()
def main():
# create a turtle to draw the frame of my graphic:
    eb = turtle.Turtle()
    eb.forward(300)
    eb.left(90)
    eb.pendown()
# draw the frame of my graphic in purple color:
    eb.pencolor((255, 153, 255))
    eb.fillcolor((255, 153, 255))
    eb.begin_fill()
    rectangle(eb, 300, 600)
    eb.end_fill()
# draw the frame of my graphic in green:
    eb.left(90)
    eb.pencolor((152, 251, 152))
    eb.fillcolor((152, 251, 152))
    eb.begin_fill()
    rectangle(eb, 600, 300)
    eb.end_fill()
    eb.penup()
# create a new turtle to draw Vietnamese flag:
    tp = turtle.Turtle()
    tp.penup()
    tp.forward(50)
    tp.right(90)
    tp.forward(180)
    tp.left(90)
    tp.pendown()
    tp.pensize(2)
    tp.pencolor((255, 0, 0))
    tp.fillcolor((255, 0, 0))
    tp.begin_fill()
    rectangle(tp, 230, 150)
    tp.end_fill()
    tp.penup()
    tp.pencolor((255,255,0))
    tp.speed(10)
    tp.left(45)
    tp.forward(120)
    tp.right(45)
    tp.pendown()
    tp.fillcolor((255,255,0))
    tp.begin_fill()
    drawStar(tp, 70)
    tp.end_fill()
    tp.penup()
# create a turtle to draw another flag:
    ebtp = turtle.Turtle()
    ebtp.pencolor("white")
    ebtp.penup()
    ebtp.left(180)
    ebtp.forward(200)
    ebtp.right(90)
    ebtp.forward(100)
    ebtp.right(90)
    ebtp.pendown()
    ebtp.fillcolor("white")
    ebtp.begin_fill()
    rectangle(ebtp,230,150)
    ebtp.end_fill()
    ebtp.pencolor((0,128,0))
    ebtp.fillcolor((0,128,0))
    ebtp.begin_fill()
    rectangle(ebtp,76,150)
    ebtp.end_fill()
    ebtp.penup()
    ebtp.forward(153)
    ebtp.pendown()
    ebtp.fillcolor((0, 128, 0))
    ebtp.begin_fill()
    rectangle(ebtp, 76, 150)
    ebtp.end_fill()
# move ebtp to write a sentence:
    ebtp.penup()
    ebtp.goto(-180, 0)
    colors=[(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130)]
    words=["I", "Love", "Being", "A ", "Creative", "Creator"]
    for i, word in enumerate(words):
        ebtp.pencolor(colors[i % 6])
        ebtp.write(word, align="left", font=("Cambria", 16, "bold"))
        ebtp.forward(len(word)*15)
    ebtp.penup()

main()

wn.exitonclick()





