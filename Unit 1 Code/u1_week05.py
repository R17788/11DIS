import turtle as t

# draw eyes
# draw nose
# draw red cheeks
# draw teeth
t.speed(0)


# move function:
def myMove(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# drawing eye
def myCircle(size, colour):
    t.fillcolor(colour)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def triangle(one, two, three):
    t.forward(one)  # draw base

    t.left(120)
    t.forward(two)

    t.left(120)
    t.forward(three)


location = t.getpen()

myCircle(100, "white")  # face

myMove(-50, 40)  # cheeks
myCircle(30, "#ff7aa4")
myMove(50, 40)
myCircle(30, "#ff7aa4")

myMove(-50, 110)
myCircle(20, "#34b7eb")  # LEFT eye
myMove(-50, 115)
myCircle(11, "white")
myMove(50, 110)
myCircle(20, "#34b7eb")  # RIGHT eye
myMove(50, 115)
myCircle(11, "white")

myMove(0, 85)  # nose
myCircle(15, "#c88265")

myMove(-50, 70)  # smile
t.seth(-90)
t.pensize(10)
t.circle(50, 180)
t.pensize(1)

myMove(-75, 175)
t.seth(0)
t.pensize(10)
t.pencolor("Brown")

for i in range(3):
    t.pendown()
    triangle(50, 50, 50)
    t.left(120)
    t.penup()
    t.forward(50)

t.ht()  # hide turtle
t.Screen().exitonclick()
