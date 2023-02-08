#######################################
# Name = Bineta Doucoure
# Username = doucoureb
# google docs link = https://docs.google.com/document/d/1PT1qGnAcvhgr-_p4A9LdAB8Xp9ItzN8vsfGRZzhbTz0/edit#
###############################################
import turtle


def function_1(t, size):
    """
    a function to get turtle t to draw a square with "size" size
    """
    for i in range(3):
        t.left(120)
        t.forward(size)


    pass
    # drawing 3 sides of the roof


def function_2(f,size):
    """
    Docstring for function_2
    """
    for i in range(4):
        f.right(90)
        f.forward(size)
    pass
    # drawing 4 sides of the body

def function_3(d,size):
    """
    Docstring for function_2
    """
    for i in range(2):
        d.forward(size)
        d.right(45)
        d.forward(size)
        d.right(135)
    pass
    # drawing petals

def function_4(d,d1,size):
    """
    Docstring for function_2
    """
    for i in range(d1):
        function_3(d,size)
        d.right(360/d1)


def main():
    """
    define two turtles and specify the properties of the turtles and the background
    """
    pass
    # draw door


    # drawing roof
    wn = turtle.Screen()
    wn.bgcolor("black")
    t = turtle.Turtle()
    t.penup()
    t.goto(0, 100)
    t.pencolor('brown')
    t.pensize(10)
    t.pendown()
    t.speed(3)
    t.left(120)
    t.end_fill()
    function_1(t, 100)            # Function call to function_1

    # drawing the body
    f = turtle.Turtle()
    f.penup()
    f.pensize(10)
    f.color('white')
    f.begin_fill()
    f.goto(-50,15)
    f.pendown()
    f.forward(100)
    f.end_fill()
    function_2(f, 100)            # Function call to function_2


    # drawing flowers
    d = turtle.Turtle()
    d.penup()
    d.goto(100,-100)
    d.pensize(2)
    d.pencolor("red")
    d.pendown()
    d.pencolor("green")
    d.left(90)
    d.forward(100)
    function_4(d,6,10)

    # drawing flowers
    d = turtle.Turtle()
    d.penup()
    d.goto(120,-100)
    d.pensize(2)
    d.pencolor("red")
    d.pendown()
    d.pencolor("green")
    d.left(90)
    d.forward(80)
    function_4(d,6,10)

    # drawing flowers
    d = turtle.Turtle()
    d.penup()
    d.goto(140,-100)
    d.pensize(2)
    d.pencolor("red")
    d.pendown()
    d.pencolor("green")
    d.left(90)
    d.forward(70)
    function_4(d,6,10)

    # drawing flowers
    d = turtle.Turtle()
    d.penup()
    d.goto(160,-100)
    d.pensize(2)
    d.pencolor("red")
    d.pendown()
    d.pencolor("green")
    d.left(90)
    d.forward(50)
    function_4(d,6,10)

    # drawing flowers
    d = turtle.Turtle()
    d.penup()
    d.goto(180,-100)
    d.pensize(2)
    d.pencolor("red")
    d.pendown()
    d.pencolor("green")
    d.left(90)
    d.forward(70)
    function_4(d,6,10)


main()




