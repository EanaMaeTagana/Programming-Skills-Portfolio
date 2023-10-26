"""
Chapter 7, Exercise 2: Favorite Book
"""
# Task: Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(favorite_book): # The parentheses are used to pass along information to the function as an argument. In this case, the name of the book.
    print("Though there are many books that I love,", favorite_book,"is one of my most favorite books ever.")
    
favorite_book("'From Lukov with Love'") # When the function is called, the name of the book is printed alongside the message.