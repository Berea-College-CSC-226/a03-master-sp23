#########################################################
# Name: Kevion Hudson
# Username: Hudsonk
# Repo Link:
# Google Doc: https://docs.google.com/document/d/1wA5BSgvcmNNwuSRoSEEnYhERsPpY-Dn2ugZcuwi6K9g/edit?usp=sharing
########################################################

import turtle

wn = turtle.Screen()
wn.bgcolor("#908cf9")
grass = turtle.Turtle()
tri = turtle.Turtle()
cir = turtle.Turtle()
sec = turtle.Turtle()
last = turtle.Turtle()
bd = turtle.Turtle()


def fill_grass():
    grass.penup()
    grass.setpos(-382, -315)
    grass.pendown()
    grass.fillcolor("green")
    grass.begin_fill()
    for i in range(2):
        grass.forward(760)
        grass.left(90)
        grass.forward(100)
        grass.left(90)
    grass.end_fill()

    def mountains():
        tri.pencolor("grey")
        tri.hideturtle()
        tri.penup()
        tri.setpos(-382, -215)
        tri.showturtle()
        tri.pendown()
        tri.begin_fill()
        tri.fillcolor("grey")
        tri.forward(200)
        tri.left(115)
        tri.forward(150)
        tri.left(110)
        tri.forward(250)
        tri.end_fill()

    def sun():
        cir.hideturtle()
        cir.color("yellow")
        cir.penup()
        cir.setpos(-182, 0)
        cir.fillcolor("yellow")
        cir.showturtle()
        cir.pendown()
        cir.right(90)
        cir.begin_fill()
        cir.circle(150)
        cir.end_fill()
        cir.hideturtle()

    def mount():
        sec.hideturtle()
        sec.penup()
        sec.pencolor("grey")
        sec.fillcolor("grey")
        sec.goto(-230, -215)
        sec.showturtle()
        sec.pendown()
        sec.begin_fill()
        sec.forward(300)
        sec.left(110)
        sec.forward(400)
        sec.left(140)
        sec.forward(400)
        sec.end_fill()
        sec.hideturtle()

    def mounts():
        last.hideturtle()
        last.penup()
        last.setpos(100, -215)
        last.color("grey")
        last.pencolor("grey")
        last.fillcolor("grey")
        last.pendown()
        last.begin_fill()
        last.left(45)
        last.forward(100)
        last.right(90)
        last.forward(50)
        last.left(90)
        last.forward(200)
        last.right(90)
        last.forward(250)
        last.end_fill()

    def birds():
        bd.shape("classic")
        bd.color("black")
        bd.penup()
        bd.setpos(40, 55)
        for g in range(5):
            bd.stamp()
            bd.forward(10)
            bd.right(90)
            bd.forward(10)
            bd.left(90)

    def main():
        fill_grass()
        mountains()
        sun()
        mount()
        mounts()
        birds()

        wn.exitonclick()

    main()
