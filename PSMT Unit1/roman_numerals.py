# Begin Program RomanNumerals
# 	Store values: [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# 	Store roman: ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
# 	Initialise numerals to empty string
# 	ask user for number between 1 and 3999
# 	If number in correct range:
# 		For i = 0 to 12:
# 			while number >= values[i]:
# 				number = number – values[i]
# 				append corresponding roman to numerals
# 			End while
# 			Increment [i]
# 		End for
# 	Else:
# 		Display error
# 	End If
# End Program RomanNumerals

values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman = ["M", "C M", "D", "C D", "C", "X C", "L", "X L", "X", "I X", "V", "I V", "I"]
repeat = True
while repeat:
    number = input("Enter a number between 1 and 3999: ")
    if not number.isdigit():
        print("Please Enter a Number")
        repeat = True

    elif 1 <= int(number) <= 3999:
        num = int(number)
        for i in range(13):
            while num >= values[i]:
                num = num - values[i]
                print(roman[i], end=" ")
        repeat = False

    else:
        print("Number too big, please enter number between 1 and 3999. ")
        repeat = True


