import turtle as t
t.speed(0)
t.screensize(4000,4000)
t.setup(1400,1000)

sum = 0
f1 = 0
f2 = 1
numberOfBubbles = 0

t.penup()
t.goto(-350,0)
t.pendown()


while numberOfBubbles < 14:
    sum = f1 + f2
    f2 = f1

    f1 = sum
    diameter = sum

    numberOfBubbles += 1
    t.circle(diameter)
    t.penup()
    t.forward(2.6*diameter)
    t.seth(-90)
    t.forward(diameter/2)
    t.seth(0)
    t.pendown()
    print(sum)
    # t.penup()
    # t.goto(diameter/2,0)
    # t.pendown()
    t.write(sum)
    # t.write("number")


# t.ht()  # hide turtle
t.Screen().exitonclick()

