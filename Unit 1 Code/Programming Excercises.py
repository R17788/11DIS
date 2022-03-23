# 	a. Design a program that displays the following information:
# 		i. Your name
# 		ii. Your address (include city, state and postcode)
# 		iii. Your telephone number
# 		iv. Your future job (name would like to become an astronaut.)
# print("Ryan Hawcroft")
# print("139 perth hills road, pearth, aus, 8913")
# print("My telephone number: 0414 219 532")
# print("Ryan would like to become president of the USA")


# 	b. Sales Prediction
# A company has determined that its annual profit is typically 23 percent of total sales.
# Design a program that asks the user to enter the projected amount of total sales and then displays the profit that
# will be made from that amount.
# Hint: Use 0.23 to represent 23 percent

# 23% of sales = annual profit

# display projectefd_profit
# input projectefd_profit
# potential profit = projected_profit times 25%
# display projected_profit

projected_profit = int(input("Enter the projected amount of total sales: "))
potential_profit = projected_profit * 0.23
print(f"The potential profit from {projected_profit} sales is {potential_profit}")

