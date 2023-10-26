"""
Chapter 5, Exercise 2: Glossary
"""
# Task: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output. 

glossary={
    "print_function": "The print function is used to print a specific statement as an output.",
    "if_statement": "The if statement evaluates a condition that if true will execute a block of code.",
    "elif_statement": "The elif function, short for 'else if', is used when the first if statement is false.",
    "while_loop": "A while loop will run a block of code as long as a given condition is true.",
    "for_loop": "A 'for' loop is used to repeat a set of code for a specified number of times.",
    }   

# The dictionary is used to store programming words as keys and their meaning as values.

print("Print Function:","\n\t",glossary["print_function"],"\nIf Statement:","\n\t",glossary["if_statement"],"\nElif Statement:","\n\t",glossary["elif_statement"],"\nWhile:","\n\t",glossary["while_loop"],"\nFor Loop:","\n\t",glossary["for_loop"])

# Each word is printed in a neat format by using the \n and \t function to add space between the words.