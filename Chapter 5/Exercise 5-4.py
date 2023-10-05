"""
Chapter 5, Exercise 4: Rivers
"""
# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

major_rivers={
    "Mississippi River": "United States",
    "Congo River": "Zambia",
    "Amur River": "China",
    }

for river, country in major_rivers.items():
    print(f"The {country.title()} has the {river.title()}.")

print("\nThe rivers that are mentioned in this data set include;")
for river in major_rivers.keys():
    print(f"{river.title()}")

print("\nThe countries that are mentioned in this data set include;")
for country in major_rivers.values():
    print(f"{country.title()}")