"""
Chapter 6, Exercise 1: Pizza Toppings
"""
# Task: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

print("Welcome to Tiny's Pizzeria!")
while True: # The while loop will run indefinitely until an if condition is added to break the cycle of the loop.
    topping=input("What toppings may we get you? \nPlease enter 'Done' once order is complete. \n") # The \n (newline) function will allow each sentence to be printed unto a different line each time it is used. On the other hand, the input function will allow for the user to enter their choice of topping.
    if topping!="Done": # If the user enters a topping, the topping will be printed in the message below and will restart the loop -- asking the user for their choice of topping.
        print(topping,"has been added to pizza!")
    else: # If user enters 'done' the program will automatically print the message and stop the loop.
        print("Pizza will be served in a couple minutes. Thank you!")
        break

