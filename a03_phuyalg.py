################################################################################
# Name: Gagan Phuyal
# Username: Phuyalg
# Repo link: https://github.com/Berea-College-CSC-226/a03-master-sp23.git
# Google Doc link: https://docs.google.com/document/d/18RLeYI_iOpa6-VQIGDKbjc8IAu8gxEOIaQUL_hGa1Yw/edit?usp=sharing
########################################################################################

# I will be drawing the Nepal Flag
import turtle

# Drawing the border for the flag
def draw_triangle(gagan, side_length):
    gagan.pensize(20)
    gagan.fillcolor("red")
    gagan.begin_fill()
    gagan.penup()
    gagan.goto(-150, 0)
    gagan.pendown()
    gagan.left(90)
    gagan.forward(side_length)
    gagan.right(120)
    gagan.forward(side_length*1.5)
    gagan.right(138)
    gagan.forward(side_length*.75)
    gagan.left(115)
    gagan.forward(side_length * 1.5)
    gagan.right(127)
    gagan.forward(294)
    gagan.right(90)
    gagan.forward(220)
    gagan.end_fill()


# Instructions to make a star shape
def draw_star(gagan,distance):
    gagan.fillcolor("#FFF198")
    n = 15
    angle = 180 - 180 / n
    for i in range(n):
        gagan.forward(distance)
        gagan.right(angle)

# Drawing the crescent part of the flag
def draw_crescent(gagan, radius, angle):
    gagan.pencolor("#FFF198")
    gagan.pensize(5)
    gagan.penup()
    gagan.goto(-120,100)
    gagan.pendown()
    gagan.right(angle)
    gagan.fillcolor("#FFF198")
    gagan.begin_fill()
    gagan.circle(radius, 180)
    gagan.end_fill()
    gagan.right(90)
    gagan.back(radius*2)
    gagan.forward(radius/4)
    gagan.pensize(5)
    draw_star(gagan,60)

# Drawing the bottom star of the flag
def draw_star_2(gagan):
        gagan.pencolor("#FFF198")
        gagan.pensize(5)
        gagan.penup()
        gagan.goto(-110,-110)
        gagan.pendown()
        draw_star(gagan,100)

# The main function which calls previous functions
def main():
    gagan = turtle.Turtle()
    wn = turtle.Screen()
    turtle.bgcolor("#DDE6E7")
    gagan.pencolor("blue")
    draw_triangle(gagan, 200)
    draw_crescent(gagan, 40, 180)
    draw_star_2(gagan)
    gagan.hideturtle()
    wn.exitonclick()
main()

