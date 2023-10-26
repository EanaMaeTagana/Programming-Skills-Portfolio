"""
Chapter 2, Exercise 5: USB Shopper
"""
# Task: A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

# The arithmetic operations that need to be done and their answers would be the following:
# 50 // 6 = 8
# 50 % 6 = 2

budget=int(input("Please enter available funds:")) # £50
amount=int(input("Please enter the cost of the item you want to buy:")) # £6 per USB 

# The input function allows for the code to get an input from the user. 
# Therefore, the user can enter their budget and the cost of the item they want to buy.

e=budget//amount
remainder=budget%amount

# Two variables are given an arithmetic operation that would be done to the user input.
# This would then allow the programme to calculate the amount of USB sticks that the girl can buy.

amount_of_USBsticks=f"You can buy an amount of '{e}' USB sticks."
print(amount_of_USBsticks)
pounds_left=f"You will have a remaining of £{remainder}."
print(pounds_left)

# The amount of USB sticks will then be shown by using the print function.
