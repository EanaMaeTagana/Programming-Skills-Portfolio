"""
Chapter 3, Exercise 7: Seeing the World
"""
# Think of at least five places in the world you’d like to visit. 
# Store the locations in a list. Make sure the list is not in alphabetical order.
# Print your list in its original order.
# Use sorted() to print your list in alphabetical order without modifying the actual list.
# Show that your list is still in its original order by printing it.
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

destinations=["Indonesia","Thailand","South Korea","Italy","Switzerland"]
print("My dream destinations that I want to visit are:")
print(destinations)

# A list named destinations is created to include a list of dream destinations.
# The list is then printed using the print function.

print("\nSorted order without modifications:")
print(sorted(destinations))

# Sorted is used to arrange items in a list in ascending order.

print("\nOriginal order:")
print(destinations)

print("\nReverse sorted without modifications:")
print(sorted(destinations, reverse=True))

# Reverse is used to reverse the arrangement of the items in a list.

print("\nOriginal order:")
print(destinations)

print("\nReverse order with modifications:")
destinations.reverse()
print(destinations)

print("\nOriginal order:")
destinations.reverse()
print(destinations)

print("\nSorted order with modifications:")
destinations.sort()
print(destinations)

print("\nReverse sorted with modifications:")
destinations.sort(reverse=True)
print(destinations)

# The function sort and reverse arranges the items in ascending order then reverses the order.
