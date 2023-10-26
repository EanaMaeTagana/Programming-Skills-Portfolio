"""
Chapter 2, Exercise 3: Stripping Names
"""
# Task: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.
# Print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

name=("\n\tTaylor Swift\n\t")

# A variable is given a person's name with some whitespace characters using \n and \t.

# Original
print("Original:")
print(name)

# The name is printed in its original form showing the whitespaces.

# Lstrip
print("Lstrip:")
print(name.lstrip())

# The same name is printed but now without the left-side whitespace.

# Rstrip
print("Rstrip:")
print(name.rstrip())

# Again, the same name is printed but now without the right-side whitespace.

# Strip
print("Strip:")
print(name.strip())

# Finally, the  name is printed but now without all the whitespace characters.
