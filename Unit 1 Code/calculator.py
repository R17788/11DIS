# create a function that takes 2 numbers and MULTIPLIES them, returning the result
def multiply(num1, num2): print(num1 * num2)


# create a function that takes 2 numbers and DIVIDES them, returning the result
def divide(num1, num2): print(num1 / num2)


# create a function that takes 2 numbers and ADDS them, returning the result
def add(num1, num2): print(num1 + num2)


# create a function that takes 2 numbers and MINUSES them, returning the result
def minus(num1, num2): print(num1 - num2)


while True:
    operation = input("Would you like to multiply, divide, add or subtract? ( m / d / a / s) ")

    if operation != "m" or operation != "d" or operation != "a" or operation != "s":
        print("")
        print(":O")
        print("")

    else:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if operation == "m":
            multiply(num1, num2)

        if operation == "d":
            divide(num1, num2)

        if operation == "a":
            add(num1, num2)

        if operation == "s":
            minus(num1, num2)

    con = input("Would you like to calculate again? (y / n) ")
    if con == "n":
        break
    else:
        continue
