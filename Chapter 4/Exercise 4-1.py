"""
Chapter 4, Exercise 1: Alien Colors #1
"""
# Task: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# The if function creates a condition, that which is true will then execute the statement or block of statements.
# Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

alien_color='green'
if alien_color=='green': 
    print("Congratulations! You earned 5 points!") 
      
# The if function is for when a condition is met, a set of code will be executed.
# The variable alien_color is green, making the if condition true. Therefore, the statement will be printed  

alien_color='red'
if alien_color=='green':
    print("Congratulations! You earned 5 points!") 
    
# The variable alien_color is red, making the if condition false. Therefore, the statement will not be printed.