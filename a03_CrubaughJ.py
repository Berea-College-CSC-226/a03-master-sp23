import turtle

wn = turtle.Screen()
wn.bgcolor("black")
fox = turtle.Turtle()
fox.color("orange")


def eqtri(x, y, s, a, c):
    fox.fillcolor(c)
    fox.penup()
    fox.goto(x, y)
    fox.begin_fill()
    fox.pendown()
    for i in range(0, 3):
        fox.forward(s)
        fox.right(a)
    fox.end_fill()


def nose(x, y, t):
    fox.penup()
    fox.goto(0, 0)
    fox.pendown()
    fox.goto(x, y)
    fox.fillcolor("white")
    fox.begin_fill()
    fox.forward(t)
    fox.forward(2 * -t)
    fox.right(60)
    fox.forward(40)
    fox.left(120)
    fox.forward(40)
    fox.end_fill()


def cir(x, y, d):
    fox.penup()
    fox.goto(x, y)
    fox.pendown()
    fox.fillcolor("black")
    fox.begin_fill()
    fox.circle(d)
    fox.end_fill()

def main():
    eqtri(-75, 0, 150, 120, "orange")
    eqtri(-75, 0, 40, -120, "orange")
    eqtri(-70, 0, 30, -120, "white")
    eqtri(35, 0, 40, -120, "orange")
    eqtri(40, 0, 30, -120, "white")

    nose(0, -95, 20)

    cir(-20, -30, 5)
    cir(20, -30, 5)

    fox.penup()
    fox.goto(300, 300)
    fox.color("black")
    wn.exitonclick()


main()
