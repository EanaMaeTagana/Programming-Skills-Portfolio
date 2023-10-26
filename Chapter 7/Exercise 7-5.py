"""
Chapter 7, Exercise 5: Cities
"""
# Task: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country='korea'): # Korea is the default value.
    msg = city.title() + " is within the borders of " + country.title() + "."
    print(msg)

describe_city('seoul') 
describe_city('tokyo', 'japan') # Tokyo is not within the default country, thus the country was specified.
describe_city('incheon')