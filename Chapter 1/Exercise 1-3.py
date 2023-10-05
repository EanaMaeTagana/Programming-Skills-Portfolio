"""
Chapter 1, Exercise 3: Print Date and Time
"""
# Write a Python program to display the current date and time

import datetime
now = datetime.datetime.now()
print ("The current date and time is:")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# The import function will retrieve the current date and time from the python libraries.