import turtle

def field():
    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    for i in range(2):
        t.forward(300)
        t.left(90)
        t.fd(500)
        t.left(90)
    t.end_fill()
r=20
def lines():
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
    t1.circle(radius=r/10)
    t1.penup()
    t1.goto(-100, 600)
def golies():
    t2 = turtle.Turtle()
    t2.penup()
    t2.goto(-120, 300)
    t2.pendown()
    t2.pencolor("#FEFDFC")
    for i in range(2):
        t2.fd(140)
        t2.right(90)
        t2.fd(70)
        t2.right(90)
    t2.right(90)
    t2.penup()
    t2.fd(430)
    t2.left(90)
    t2.pendown()
    for i in range(2):
        t2.fd(140)
        t2.right(90)
        t2.fd(70)
        t2.right(90)
    t2.fd(110)
    t2.left(90)
    t2.circle(40,180)
    t2.left(180)
    t2.penup()
    t2.fd(359)
    t2.right(180)
    t2.pendown()
    t2.circle(40, 180)













def main():
    win = turtle.Screen()
    turtle.Screen().bgcolor("#196F3D")
    field()
    lines()
    golies()
    win.exitonclick()

main()