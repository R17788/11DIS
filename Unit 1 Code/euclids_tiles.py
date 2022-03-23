num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
fnum = None
snum = None

fnum = num1  # First Number
snum = num2  # Second Number
# def euclids_algorithm(num1, num2):

num3 = None

print("")

while num1 != 0 and num2 != 0 and num3 != 0:

    num3 = num1 % num2

    if num3 == 0:
        break

    num1 = num2 % num3

    if num1 == 0:
        break

if num1 != 0:
    print(num1)
if num3 != 0:
    print(num3)



# euclids_algorithm(num1, num2)
# num3 = 15

import turtle as t
t.hideturtle()

t.speed(0)


def myMove(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def myPen(col, size):
    t.color(col)
    t.pensize(size)


length = snum
width = fnum

t.screensize(length, width)
t.setup(500, 500)

myMove(-(length / 2), (width / 2))


myPen('#4287f5', 5)
t.forward(length)
t.seth(-90)
t.forward(width)
t.seth(180)
t.forward(length)
t.seth(90)
t.forward(width)


NoBL = length // num3  # NoBL = Number of Boxes Length
NoBW = width // num3  # NoBW = Number of Boxes Width
BS = num3
myPen('#4287f5', 2)
for i in range(NoBW):

    for f in range(NoBL):  # 23 NoBL
        t.seth(0)
        t.forward(num3)
        t.seth(-90)
        t.forward(num3)
        t.seth(180)
        t.forward(num3)
        t.seth(90)
        t.forward(num3)
        t.seth(0)
        t.forward(num3)

    side_length = length // 2
    side_width = (width // 2) - BS
    BS += num3
    myMove(-side_length, side_width)

myMove(-(length / 2), (width / 2))



t.Screen().exitonclick()
