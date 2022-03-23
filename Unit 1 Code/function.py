# num = int(input("Enter a number: "))

def rangecheck(num):  # this is called a function declaration
    min = 0
    max = 100

    for i in range(min, max):  # loop that continues for a known number of iterations
        # print(i)

        # if num in range(0,100):
        if min < num < max:  # conditional statement
            print(num)
            break  # exit will exit the current program, break will exit the current loop
        else:
            print(f"Number {num} not in range {min} to {max}.")
            break


# once I have created a function, I need to create a function call

# rangecheck(140)
# rangecheck(120)

for i in range(1, 50):
    a = i
    b = i * 10
    rangecheck(a)
    rangecheck(b)
    a ** i
    b ** i
