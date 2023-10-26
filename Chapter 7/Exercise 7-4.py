"""
Chapter 7, Exercise 4: Large Shirts
"""
# Task: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size="large", message="I love python"): # Within the parentheses, the sizes and message are set -- making the size and message default.
    print("This shirt will be size",size+".")
    print("It will have the message '"+message+"' printed unto it.")
    
make_shirt() # Calling back the function will print the default message with the default size -- large.
make_shirt(size="medium") # This time, the size is specified to medium. Thus, when the function is called, the size will now be medium but with the same message.
make_shirt(size="small", message="I love studying python") # Now, this shirt contains a different size and message.