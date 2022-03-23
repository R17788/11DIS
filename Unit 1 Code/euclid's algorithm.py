num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


def euclids_algorithm(num1, num2):
    num3 = None

    print("")

    while num3 != 0:

        num3 = num1 % num2
        print("num3", num3)

        if num3 == 0:
            break

        num1 = num2 % num3
        print("num1", num1)

        if num1 == 0:
            break

        num2 = num3 % num1
        print("num2", num2)

        if num2 == 0:
            break


# print(1112%695) = 417
# print(695%417) = 278
# print(417%278) = 139
# print(278%139) = 0

euclids_algorithm(num1, num2)
