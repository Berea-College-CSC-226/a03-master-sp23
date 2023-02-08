import turtle
wn = turtle.Screen()
love = turtle.Turtle()
house = turtle.Turtle()
top = turtle.Turtle()
wn.bgcolor("yellow")
love.pencolor("pink")
love.penup()
love.goto(-0, -250)

def love_vals():
    for i in range(2):
        love.penup()
        love.goto(-150, -50)
        love.pendown()
        love.fillcolor("red")
        love.begin_fill()
        love.pensize(2)
        love.left(50)
        love.forward(133)
        love.circle(50, 200)
        love.right(140)
        love.circle(50, 200)
        love.forward(133)
        love.end_fill()

def house_features():
    house.penup()
    house.goto(50, -50)
    house.pendown()
    house.pensize(6)
    house.color("blue")
    for i in range(4):
        house.fd(120)
        house.left(90)
        house.fd(120)
        house.left(90)
def house_top():
    for i in range(2):
        top.penup()
        top.goto(60, -50)
        top.pendown()
        top.fillcolor("brown")
        top.begin_fill()
        top.pensize(8)
        top.right(45)
        top.forward(200)
        top.right(90)
        top.forward(200)
        top.left(180)
        top.forward(200)
        top.right(135)
        top.forward(259)
        top.right(90)
        top.forward(142)
        top.end_fill()


def main():
    love_vals()
    house_features()
    house_top()

if __name__ == "__main__":
    main()
