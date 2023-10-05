"""
Chapter 5, Exercise 3: Glossary #2
"""
# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 
# When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.

glossary={
    "Print Function": "The print function is used to print a specific statement as an output.",
    "If Statement": "The if statement evaluates a condition that if true will execute a block of code.",
    "Elif Statement": "The elif function, short for 'else if', is used when the first if statement is false.",
    "While Loop": "A while loop will run a block of code as long as a given condition is true.",
    "For Loop": "A 'for' loop is used to repeat a set of code for a specified number of times.",
    "Variable": "A variable is a placeholder name for a value",
    "String": "A string is a data type which includes words and characters.",
    "Integer": "An integer is data type which is a whole number with no decimals.",
    "Float": "A float is a data type which is a number that can have a decimal value.",
    "Boolean": "A boolean is a data type which represents one of two values which is either true or false."
    }  

for i in glossary:
    print(i,":",glossary[i])