############################################################
# Name: Abdallahi hamdy
# Username: hamdya
# Repo Link: https://docs.google.com/document/d/1D_f3fJDvhS_BKacHKS7SOwkoEvEG6m-qVFAHYESeqoM/edit?usp=sharing
# Github Link: https://github.com/Berea-College-CSC-226/a03-master-sp23.git
############################################################

import turtle

def rectangle(house, init_point, point_one, point_two, point_three):
    house.begin_fill()
    house.penup()
    house.goto(init_point)
    house.pendown()
    house.goto(point_one)
    house.goto(point_two)
    house.goto(point_three)
    house.goto(init_point)
    house.end_fill()

def half_circle(house, init_point, raduis, degree):
    house.begin_fill()
    house.penup()
    house.goto(init_point)
    house.left(90)
    house.pendown()
    house.circle(raduis, degree)
    house.penup()
    house.goto(init_point)
    house.end_fill()

def shop_placket(house, init_point, height):
    house.begin_fill()
    house.penup()
    house.goto(init_point)
    house.pendown()
    house.right(90)
    house.forward(height)
    for i in range(10):
        house.circle(15, 180)
        house.right(180)
    house.left(180)
    house.forward(height)
    house.left(90)
    house.forward(300)
    house.end_fill()


def main():
    # window & turtle setup
    house = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("black")
    house.speed(0)

    # ground attribute
    house.color("black", "grey")

    rectangle(house, (-200, -275), (-200, -200), (200, -200), (200, -275))


    # sky attribute
    house.color("black", "lightblue")

    rectangle(house, (-200, -200), (-200, 300), (200, 300), (200, -200))


    # orange structure attribute
    house.color("black", "orange")

    rectangle(house, (-133, -200), (-133, 200), (133, 200), (133, -200))


    # structure red top attribute
    house.color("black", "red")

    rectangle(house, (-155, 200), (-155, 250), (155, 250), (155, 200))


    # structure rect. door pamphlet attribute
    house.color("black", "red")

    rectangle(house, (-150, 20), (-133, 90), (133, 90), (150, 20))


    # structure placket attribute
    house.color("black", "red")

    shop_placket(house, (-150, 20), 20)


    # structure shop name
    house.penup()
    house.goto(0,30)
    house.pendown()
    house.write("Cafe", align="center", font=("Lucida Sans", 30, 'normal'))


    # structure chimney attribute
    house.color("black", "gray")

    rectangle(house, (-105, 250), (-105, 275), (-80, 275), (-80, 250))


    # structure rect. door attribute
    house.color("black", "red")

    rectangle(house, (30, -200), (30, -70), (110, -70), (110, -200))


    # door edit
    house.color("red")
    house.penup()
    house.goto((30, -70))
    house.pendown()
    house.goto((110, -70))


    # structure door top attribute
    house.color("black", "red")
    house.left(180)

    half_circle(house, (110, -70), 40, 180)


    # structure door window top attribute
    house.color("black", "yellow")

    rectangle(house, (50, -80), (70, -60), (90, -80), (70, -100))


    # structure door knob
    house.color("black", "red")

    house.penup()
    house.goto(95, -130)
    house.pendown()

    house.circle(5, 360)


    # structure big window bottom attribute
    house.color("black", "yellow")

    rectangle(house, (-100, -150), (-100, -100), (0, -100), (0, -150))


    # structure big window top attribute
    house.color("black", "yellow")
    house.left(90)

    half_circle(house, (0, -100), 50, 180)


    # window 1 edit
    house.color("black")
    house.penup()
    house.goto(-50, -150)
    house.pendown()
    house.goto(-50, -50)

    # structure small window 1 bottom attribute
    house.color("black", "yellow")

    rectangle(house, (-100, 150), (-100, 125), (-50, 125), (-50, 150))


    # structure small window 1 top attribute
    house.color("black", "yellow")
    house.left(90)

    half_circle(house, (-50, 150), 25, 180)


    # window 1 edit
    house.color("black")
    house.penup()
    house.goto(-75, 125)
    house.pendown()
    house.goto(-75, 175)


    # structure small window 2 bottom attribute
    house.color("black", "yellow")

    rectangle(house, (-25, 150), (-25, 125), (25, 125), (25, 150))


    # structure small window 2 top attribute
    house.color("black", "yellow")
    house.left(90)

    half_circle(house, (25, 150), 25, 180)


    # window 2 edit
    house.color("black")
    house.penup()
    house.goto(0, 125)
    house.pendown()
    house.goto(0, 175)


    # structure small window 3 bottom attribute
    house.color("black", "yellow")

    rectangle(house, (100, 150), (100, 125), (50, 125), (50, 150))


    # structure small window 3 top attribute
    house.color("black", "yellow")
    house.left(90)

    half_circle(house, (100, 150), 25, 180)


    # window 3 edit
    house.color("black")
    house.penup()
    house.goto(75, 125)
    house.pendown()
    house.goto(75, 175)

    house.hideturtle()

    wn.exitonclick()

main()