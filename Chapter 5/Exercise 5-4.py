"""
Chapter 5, Exercise 4: Rivers
"""
# Task: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

major_rivers={
    "Mississippi River": "United States",
    "Congo River": "Zambia",
    "Amur River": "China",
    }

# A dictionary is used to store major rivers and their countries as key and value sets.

for river, country in major_rivers.items():
    print(f"The {country.title()} has the {river.title()}.")
    
# The for loop function is used to print the statement showing which country has which river.

print("\nThe rivers that are mentioned in this data set include;")
for river in major_rivers.keys():
    print(f"{river.title()}")

print("\nThe countries that are mentioned in this data set include;")
for country in major_rivers.values():
    print(f"{country.title()}")
    
# Finally, the for loop is used to print the rivers and countries that are mentioned in the data set.