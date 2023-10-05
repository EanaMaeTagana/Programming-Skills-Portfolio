"""
Chapter 4, Exercise 2: Alien Colors #2
"""

# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# Write one version of this program that runs the if block and another that runs the else block.

# If block

alien_color='green'
if alien_color == 'green':
    print("Congratulations! You earned 5 points!")
else:
    print("Congratulations! You earned 10 points!") # Because the if condition is true, the first statement will be printed.
    
# Else block

alien_color='red'
if alien_color == 'green':
    print("Congratulations! You earned 5 points!")
else:
    print("Congratulations! You earned 10 points!") # Because the if condition is false and the else condition is true, the second statement will be printed.
    
    