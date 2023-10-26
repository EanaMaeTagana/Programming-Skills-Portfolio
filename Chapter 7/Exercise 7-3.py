"""
Chapter 7, Exercise 3: T-Shirt
"""
# Task: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message): # Two arguments are included.
    print("This shirt will be size", size+".")
    print("It will have the message '"+message+"' printed unto it.")
    
make_shirt("extra large","love, peace, and joy") # This time, the function is called using positional arguments. This means that the arguments have to be listed in the order which it was listed as initially.
make_shirt(message="love, peace, and joy", size="extra extra small") # By using keyword arguments, the arguments are identified through parameter names that are specified.