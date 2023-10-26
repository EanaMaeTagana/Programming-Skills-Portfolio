"""
Chapter 4, Exercise 3: Alien Colors #3
"""
# Task: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# Write three versions of this program, making sure each message is printed for the appropriate color alien.
    # If the alien is green, print a message that the player earned 5 points.
    # If the alien is yellow, print a message that the player earned 10 points.
    # If the alien is red, print a message that the player earned 15 points.

alien_color='green'
if alien_color == 'green':
    print("Congratulations! You earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations! You earned 10 points!")
elif alien_color == 'red':
    print("Congratulations! You earned 15 points!")
    
# The elif function is used for when the first condition is not met and there is another condition that can be evaluated.
# Because the value is set to green, the first condition is met. Therefore, the  succeeding statement will be printed.

alien_color='yellow'
if alien_color == 'green':
    print("Congratulations! You earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations! You earned 10 points!")
elif alien_color == 'red':
    print("Congratulations! You earned 15 points!")
    
# Because the value is set to yellow, the second condition is met. Therefore, the succeeding statement will be printed.
    
alien_color='red'
if alien_color == 'green':
    print("Congratulations! You earned 5 points!")
elif alien_color == 'yellow':
    print("Congratulations! You earned 10 points!")
elif alien_color == 'red':
    print("Congratulations! You earned 15 points!")
    
# Because the value is set to red, the third condition is met. Therefore, the succeeding statement will be printed.