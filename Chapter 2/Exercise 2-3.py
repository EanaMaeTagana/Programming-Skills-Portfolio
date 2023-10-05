"""
Chapter 2, Exercise 3: Stripping Names
"""
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name.

name=("\n\tTaylor Swift\n\t")
print("Original:")
print(name)

# Print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

# Lstrip
print("Lstrip:")
print(name.lstrip())

# Rstrip
print("Rstrip:")
print(name.rstrip())

# Strip
print("Strip:")
print(name.strip())
