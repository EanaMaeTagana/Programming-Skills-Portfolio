"""
Chapter 7, Exercise 4: Large Shirts
"""
# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size="large", message="Metalica"):
    print("I am going to be making a shirt that is size",size+".")
    print("It will have the words", message, "printed unto it.")
    
make_shirt()
make_shirt(size="medium")
make_shirt("small", "five seconds of summer")