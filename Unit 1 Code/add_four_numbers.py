# This program should first ask for four numbers, then add them, then print the output.

number1 = None
number2 = None
number3 = None
number4 = None
total = None



def add_four_numbers(number1, number2, number3, number4):
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
    number3 = int(input("Enter a number: "))
    number4 = int(input("Enter a number: "))

    total = number1 + number2 + number3 + number4
    print("")
    print(f"Your total is {total}")


add_four_numbers(number1, number2, number3, number4)


