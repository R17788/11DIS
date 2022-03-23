num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = None

print("")

while num3 != 0:

    num3 = num1%num2
    print(num3)

    if num3 == 0:
        break

    num1 = num2%num3
    print(num1)

    if num1 == 0:
        break

    num2 = num3%num1
    print(num2)

    if num2 == 0:
        break

print("")

if num3 != 0:
    print(f"The answer is {num3}")

elif num2 != 0:
    print(f"The answer is {num2}")

elif num1 != 0:
    print(f"The answer is {num1}")


