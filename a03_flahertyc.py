import turtle
wn = turtle.Screen()
tod = turtle.Turtle()
bob = turtle.Turtle()
# color pallet
# red (255, 0, 0)
# fancy green (100, 200, 50)
# blue(100,100,200)
# window blue(100, 150, 255)
# brown (165, 42, 42)
# other brown (218, 160, 109)
def grass():
    bob.fillcolor(100, 200, 50)
    bob.forward(-1000)
    bob.begin_fill()
    for i in range(4):
        bob.forward(2000)
        bob.left(-90)
    bob.end_fill()
def box():
    tod.fillcolor(255, 0, 0)
    tod.begin_fill()
    for i in range(4):
        tod.forward(100)
        tod.left(90)
    tod.end_fill()
def tri():
    tod.fillcolor(100,100,200)
    tod.begin_fill()
    for i in range(3):
        tod.forward(100)
        tod.left(120)
    tod.end_fill()
def chim():
    tod.fillcolor(165, 42, 42)
    tod.begin_fill()
    for i in range(4):
        l = 0
        if i % 2 == 0:
            l = 20
        else:
            l = 50
        tod.forward(l)
        tod.left(90)

    tod.end_fill()
def window():
    tod.fillcolor(100, 150, 255)
    tod.begin_fill()
    for i in range(4):
        tod.forward(20)
        tod.left(90)
    tod.end_fill()
def door():
    tod.fillcolor(218, 160, 109)
    tod.begin_fill()
    for i in range(4):
        l = 0
        if i % 2 == 0:
            l = 20
        else:
            l = 50
        tod.forward(l)
        tod.left(90)
    tod.end_fill()
def house():
    box()

    tod.penup()
    tod.left(90)
    tod.forward(100)
    tod.left(-90)
    tod.pendown()

    tri()

    tod.penup()
    tod.forward(80)
    tod.pendown()

    chim()

    tod.penup()
    tod.forward(20)
    tod.right(90)
    tod.forward(100)
    tod.right(90)
    tod.forward(60)
    tod.right(180)
    tod.pendown()

    door()

    tod.penup()
    tod.forward(35)
    tod.left(90)
    tod.forward(50)
    tod.right(90)
    tod.pendown()

    window()

    tod.left(90)
    tod.forward(10)
    tod.right(90)
    tod.forward(20)
    tod.forward(-10)
    tod.left(90)
    tod.forward(10)
    tod.forward(-20)
def main():
    wn.colormode(255)
    wn.bgcolor(200, 0, 255)
    tod.speed(10)
    tod.hideturtle()
    grass()
    house()

    wn.exitonclick()
main()