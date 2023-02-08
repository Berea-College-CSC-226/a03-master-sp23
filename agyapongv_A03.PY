import turtle
wn = turtle.Screen()
love = turtle.Turtle()
house = turtle.Turtle()

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
        love.pensize(8)
        love.left(50)
        love.forward(133)
        love.circle(50, 200)
        love.right(140)
        love.circle(50, 200)
        love.forward(133)
        love.end_fill()

def house_features(turtle, height):
    house.penup()
    house.goto(-230, -228)
    house.pendown()
    house.pensize(26)
    house.color("blue")
    for i in range(2):
        house.fd(120)
        house.left(90)
        height.fd(75)
        house.left(90)

def main():
    love_vals()
    house_features(house, 75)
    turtle.done()

if __name__ == "__main__":
    main()
