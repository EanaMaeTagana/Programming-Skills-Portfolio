"""
Chapter 3, Exercise 3: Your Own List
"""
# Task: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

transportation=["car","bus","metro","jeep","motorcycle"]

# A variable named transportation is given a list of different modes of transportation.

message="Using the "+transportation[0]+" is the most efficient method of transportation."
print(message)
message="Most of the time, I use the "+transportation[1]+" before I can go to the metro station."
print(message)
message="Using the "+transportation[2]+" can be a little hard sometimes because of rush hour."
print(message)
message="I would like to own a "+transportation[3]+" wrangler one day, preferrably in white."
print(message)
message="I once rode a "+transportation[4]+" when I was younger, it was very fun."
print(message)

# Using the message 'variable', each item of the list is given a personalized statement.
# Each message is then printed one by one.