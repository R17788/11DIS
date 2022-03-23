operation = input("Would you like to multiply, divide, add or subtract? ( m / d / a / s) ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


# create a function that takes 2 numbers and MULTIPLIES them, returning the result
def multiply(num1, num2): print(num1 * num2)


# create a function that takes 2 numbers and DIVIDES them, returning the result
def divide(num1, num2): print(num1 / num2)


# create a function that takes 2 numbers and ADDS them, returning the result
def add(num1, num2): print(num1 + num2)


# create a function that takes 2 numbers and MINUSES them, returning the result
def subtract(num1, num2): print(num1 - num2)


if operation == "m":
    multiply

if operation == "d":
    divide

if operation == "a":
    add

if operation == "s":
    subtract
